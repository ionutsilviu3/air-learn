# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired

class ContentUploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content_type = SelectField('Content Type', choices=[
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('scorm', 'SCORM')
    ], validators=[DataRequired()])
    content_text = TextAreaField('Text Content')
    content_file = FileField('Media File')
    pdf_text = TextAreaField('PDF Text')  # For PDF content
    scorm_manifest_file = FileField('SCORM Manifest File')  # For SCORM content
    video_caption = StringField('Video Caption')  # For video content
