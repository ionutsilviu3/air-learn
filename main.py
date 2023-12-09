from flask import Flask, render_template

app = Flask(__name__)

# Sample data (replace with your actual data)
courses = [
    {"id": 1, "title": "Introduction to Programming", "videos": ["video1.mp4", "video2.mp4"]},
    {"id": 2, "title": "Web Development Basics", "videos": ["video3.mp4", "video4.mp4"]},
]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course(course_id):
    course = next((c for c in courses if c["id"] == course_id), None)
    if course:
        return render_template('course.html', course=course)
    return "Course not found", 404

if __name__ == '__main__':
    app.run(debug=True)
