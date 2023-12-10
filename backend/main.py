from model import db, Video, Course
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airlearn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it is not needed for this example

db.init_app(app)

# Create tables when the application starts (only for development)
with app.app_context():
    db.create_all()

@app.route('/api/videos', methods=['GET'])
def get_all_videos():
    new_video = Video.add_video(
    title='Introduction to Neural Networks',
    description='Learn the basics of Neural Networks.',
    thumbnail_url='/images/thumbnail.jpg',
    video_url='/videos/NeuralNetworks.mp4'
)
    
    videos = Video.query.all()
    return jsonify([video.serialize() for video in videos])
   
@app.route('/') 
@app.route('/templates/home.html')
def index():
    return render_template('home.html')

@app.route('/templates/about.html')
def about():
    return render_template("about.html")

@app.route('/templates/courses.html')
def courses():
    courses_data = Course.query.all()
    return render_template('courses.html', courses_data=courses_data)


if __name__ == '__main__':
    
    with app.app_context():
        # Drop and recreate the tables (for development purposes)
        db.drop_all()
        db.create_all()

        # Populate the database with sample data
        course1 = Course(
            tutor_image_url='../static/images/download.jpg',
            tutor_name='Costel Aldea',
            tutor_date='21-11-2023',
            course_thumbnail_url='../static/images/thumbnail.jpg',
            course_title='Complete HTML Tutorial',
            course_playlist_url='/playlist/course1'
        )

        db.session.add(course1)
        db.session.commit()
    
    app.run(debug=True)
