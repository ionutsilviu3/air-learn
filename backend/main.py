from model import db, Video
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it is not needed for this example

db.init_app(app)

# Create tables when the application starts (only for development)
with app.app_context():
    db.create_all()

@app.route('/api/videos', methods=['GET'])
def get_all_videos():
    new_video = Video.add_video(
    title='Introduction to Flask',
    description='Learn the basics of Flask web framework.',
    thumbnail_url='/images/thumbnail.jpg',
    video_url='/videos/video.mp4'
)
    
    videos = Video.query.all()
    return jsonify([video.serialize() for video in videos])
   
@app.route('/') 
@app.route('/home.html')
def index():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/courses.html')
def courses():
    return render_template("courses.html")

if __name__ == '__main__':
    app.run(debug=True)
