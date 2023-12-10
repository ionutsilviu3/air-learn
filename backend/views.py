
from flask import Flask, app, flash, redirect, render_template, url_for
from werkzeug.utils import secure_filename
import os
from backend.s3_utils import upload_file_to_s3
from model import *
from forms import ContentUploadForm
import boto3
import configparser

ALLOWED_EXTENSIONS = {'pdf', 'mp4', 'lsm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_content/<int:course_id>', methods=['GET', 'POST'])
def upload_content(course_id):
    form = ContentUploadForm()
    course = Course.query.get_or_404(course_id)

    if form.validate_on_submit():
        content_type = form.content_type.data

        if content_type in {'text', 'image', 'audio'}:
            # Handle non-file content as before
            content = Content(course=course, content_type=content_type, content_text=form.content_text.data)
        else:
            file = form.content_file.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                content_url = upload_file_to_s3(file, filename)
                content = Content(course=course, content_type=content_type, content_url=content_url)
                # Set specific fields for each content type
                if content_type == 'pdf':
                    content.pdf_text = form.pdf_text.data
                elif content_type == 'scorm':
                    # Handle SCORM content (upload manifest file to S3, set scorm_manifest_url)
                    scorm_manifest_url = upload_file_to_s3(form.scorm_manifest_file.data, secure_filename(form.scorm_manifest_file.data.filename))
                    content.scorm_manifest_url = scorm_manifest_url
                elif content_type == 'video':
                    content.video_caption = form.video_caption.data

                db.session.add(content)
                db.session.commit()
                flash('Content uploaded successfully!', 'success')
                return redirect(url_for('upload_content', course_id=course_id))
            else:
                flash('Invalid file format!', 'error')

    return render_template('upload_content.html', form=form, course=course)

@app.route('/home')
def home():
    config = configparser.ConfigParser()
    config.read('credentials.ini')

    aws_access_key_id = config.get('AWS', 'access_key_id')
    aws_secret_access_key = config.get('AWS', 'secret_access_key')
    aws_bucket = config.get('AWS', 's3_bucket')

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Query all courses from your database
    courses_data = Course.query.all()

    # Update the tutor_image_url, course_thumbnail_url, and course_playlist_url with S3 URLs
    for course in courses_data:
        course.tutor_image_url = get_s3_url(s3, aws_bucket, course.tutor_image_url)
        course.course_thumbnail_url = get_s3_url(s3, aws_bucket, course.course_thumbnail_url)
        course.course_playlist_url = get_s3_url(s3, aws_bucket, course.course_playlist_url)

    return render_template('home.html', courses_data=courses_data)

def get_s3_url(s3, bucket_name, key):
    # Generate a pre-signed URL for the S3 object
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': key},
        ExpiresIn=3600  # URL expires in 1 hour, adjust as needed
    )
    return url