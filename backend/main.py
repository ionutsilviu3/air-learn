from model import db
from flask import Flask, render_template, jsonify
import os
from urllib.parse import unquote

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airlearn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it is not needed for this example
db.init_app(app)

# # Create tables when the application starts (only for development)
with app.app_context():
    db.create_all()
   
@app.route('/')
@app.route('/templates/home.html')
def home():
    return render_template("home.html")

@app.route('/templates/about.html')
def about():
    return render_template("about.html")

@app.route('/templates/profile.html')
def profile():
    return render_template("profile.html")

@app.route('/templates/login.html')
def login():
    return render_template("login.html")

@app.route('/templates/register.html')
def register():
    return render_template("register.html")

@app.route('/templates/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/templates/update.html')
def update():
    return render_template("update.html")

@app.route('/templates/teachers.html')
def teachers():
    return render_template("teachers.html")

@app.route('/templates/teachers_profile.html')
def teachers_profile():
    return render_template("teachers_profile.html")

@app.route('/templates/upload_videos.html')
def upload_videos():
    return render_template("upload_videos.html")


def get_course_info(professor_name, course_title):
    base_path = '/static/data/'
    professor_path = base_path + unquote(professor_name)
    course_path = unquote(professor_path) + '/' + unquote(course_title)
    
    # Fix the paths for video and pdf
    video_path = course_path + '/video/video.mp4'
    pdf_path = course_path + '/pdf/pdf.pdf'
    
    thumbnail_path = course_path + '/thumbnail.jpg'
    
    course_info = {
        'professor_name': professor_name,
        'course_title': course_title,
        'video_path': video_path,
        'pdf_path': pdf_path,
        'thumbnail_path': thumbnail_path
    }

    return course_info


@app.route('/video/<professor_name>/<course_title>')
def video(professor_name, course_title):
    # Assuming you have a function to retrieve course information
    course = get_course_info(professor_name, course_title)
    return render_template('video.html', course=course)

@app.route('/templates/courses.html')
def courses():
    courses_data = []
    
    for professor in os.listdir('static/data/'):
        for course_title in os.listdir('static/data/' + professor):
            video_path = '/static/data/' + professor + '/' + course_title + '/video/video.mp4'
            pdf_path = '/static/data/' + professor + '/' + course_title + '/pdf/pdf.pdf'
            thumbnail_path = '/static/data/' + professor + '/' + course_title + '/thumbnail.jpg'
            course_info = {
            'professor_name': professor,
            'course_title': course_title,
            'video_path': video_path,
            'pdf_path': pdf_path,
            'thumbnail_path': thumbnail_path
        }
        courses_data.append(course_info)   

    return render_template('courses.html', courses_data=courses_data)

# def populate(professor_name, course_title, video_path, thumbnail_path):
#     professor = os.listdir('static/data/')[0]
#     #     professors_folder.add('data/' + professor_name)
#     # Populate the database with sample data
#     course_info = Course(
#     professor_name = professor,
#     course_title = 'PHP',
#     video_path = '/static/data/Costel Aldea/php/video/video.mp4',
#     thumbnail_path= '/static/data/Costel Aldea/php/thumbnail.jpg'
#     )

#     db.session.add(course_info)
#     db.session.commit()

if __name__ == '__main__':
    
    with app.app_context():
        # Drop and recreate the tables (for development purposes)
        db.drop_all()
        db.create_all()

    app.run(debug=True)