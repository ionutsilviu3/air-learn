from model import db, Course
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airlearn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it is not needed for this example
#app.config['UPLOAD_FOLDER'] = 'data'
db.init_app(app)

# # Create tables when the application starts (only for development)
with app.app_context():
    db.create_all()

# @app.route('/api/videos', methods=['GET'])
# def get_all_videos():
#     new_video = Video.add_video(
#     title='Introduction to Neural Networks',
#     description='Learn the basics of Neural Networks.',
#     thumbnail_url='/images/thumbnail.jpg',
#     video_url='/videos/NeuralNetworks.mp4'
# )
    
#     videos = Video.query.all()
#     return jsonify([video.serialize() for video in videos])
   
@app.route('/')
@app.route('/templates/home')
def home():
    return render_template("home.html")

@app.route('/templates/about')
def about():
    return render_template("about.html")

@app.route('/templates/profile')
def profile():
    return render_template("profile.html")

@app.route('/templates/login')
def login():
    return render_template("login.html")

@app.route('/templates/register')
def register():
    return render_template("register.html")

@app.route('/templates/courses.html')
def courses():
    courses_data = []
    professors_folder = []
    
    # for professor_name in os.listdir('' + app.config['UPLOAD_FOLDER']):
    #     professors_folder.add('data/' + professor_name)

    #     for course_title in os.listdir(professors_folder):
    #         course_folder = os.path.join(professors_folder, course_title)
    #         videos = [f for f in os.listdir(course_folder) if f.endswith('.mp4')]
    #         pdfs = [f for f in os.listdir(course_folder) if f.endswith('.pdf')]

            # if videos:  # Check if there are videos in the course
            #     video_path = os.path.join(course_folder, videos[0])  # Assume the first video is the main one
            #     thumbnail_path = os.path.join(course_folder, 'thumbnail.jpg')  # Adjust as needed
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
    #     professors_folder.add('data/' + professor_name)
    # Populate the database with sample data
    

    return render_template('courses.html', courses_data=courses_data)

def get_data_from_files():
    professor_name = ''
    course_title = ''
    video_path = ''
    thumbnail_path = ''
    return professor_name, course_title, video_path, thumbnail_path

def populate(professor_name, course_title, video_path, thumbnail_path):
    professor = os.listdir('static/data/')[0]
    #     professors_folder.add('data/' + professor_name)
    # Populate the database with sample data
    course_info = Course(
    professor_name = professor,
    course_title = 'PHP',
    video_path = '/static/data/Costel Aldea/php/video/video.mp4',
    thumbnail_path= '/static/data/Costel Aldea/php/thumbnail.jpg'
    )

    db.session.add(course_info)
    db.session.commit()

if __name__ == '__main__':
    
    with app.app_context():
        # Drop and recreate the tables (for development purposes)
        db.drop_all()
        db.create_all()

        populate('','','','')
    
    app.run(debug=True)