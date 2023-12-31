from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_name = db.Column(db.String(100))
    course_title = db.Column(db.String(255))
    video_path = db.Column(db.String(200))
    pdf_path = db.Column(db.String(200))
    thumbnail_path = db.Column(db.String(200))

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    thumbnail_url = db.Column(db.String(255), nullable=True)
    video_url = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'thumbnail_url': self.thumbnail_url,
            'video_url': self.video_url
        }
    @classmethod
    def add_video(cls, title, description, thumbnail_url, video_url):
        new_video = cls(
            title=title,
            description=description,
            thumbnail_url=thumbnail_url,
            video_url=video_url
        )
        db.session.add(new_video)
        db.session.commit()
        return new_video

    @classmethod
    def remove_video(cls, video_id):
        video_to_remove = cls.query.get(video_id)
        if video_to_remove:
            db.session.delete(video_to_remove)
            db.session.commit()
            return True
        return False
    
# class User(db.Model):
#     id = db.column(db.Integer(), primary_key=True)
#     name = db.column(db.String(length=30), nullable=False,unique=True)
#     name = db.column(db.String(length=300), nullable=True)
    
#     def __repr__(self):
#         return f'User {User.name}'

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     professor_name = db.Column(db.String(100))
#     course_title = db.Column(db.String(100))
#     video_filename = db.Column(db.String(255))  # Store the video file name
#     pdf_filename = db.Column(db.String(255))  # Store the pdf file name

# class Content(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content_type = db.Column(db.String(20))  # 'text', 'image', 'audio', 'video', 'pdf', 'scorm'
#     content_text = db.Column(db.Text)  # Only for 'text' content
#     content_url = db.Column(db.String(255))  # URL or key to the stored media file on S3
#     pdf_text = db.Column(db.Text)  # Text content for PDFs
#     scorm_manifest_url = db.Column(db.String(255))  # URL to the SCORM manifest file
#     video_caption = db.Column(db.String(255))  # Caption for videos
#     course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)


# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tutor_image_url = db.Column(db.String(255))
#     tutor_name = db.Column(db.String(100))
#     tutor_date = db.Column(db.String(20))
#     course_thumbnail_url = db.Column(db.String(255))
#     course_title = db.Column(db.String(100))
#     course_playlist_url = db.Column(db.String(100))

# class Video(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     thumbnail_url = db.Column(db.String(255), nullable=True)
#     video_url = db.Column(db.String(255), nullable=False)

#     def serialize(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'description': self.description,
#             'thumbnail_url': self.thumbnail_url,
#             'video_url': self.video_url
#         }
#     @classmethod
#     def add_video(cls, title, description, thumbnail_url, video_url):
#         new_video = cls(
#             title=title,
#             description=description,
#             thumbnail_url=thumbnail_url,
#             video_url=video_url
#         )
#         db.session.add(new_video)
#         db.session.commit()
#         return new_video

#     @classmethod
#     def remove_video(cls, video_id):
#         video_to_remove = cls.query.get(video_id)
#         if video_to_remove:
#             db.session.delete(video_to_remove)
#             db.session.commit()
#             return True
#         return False
    
# # class User(db.Model):
# #     id = db.column(db.Integer(), primary_key=True)
# #     name = db.column(db.String(length=30), nullable=False,unique=True)
# #     name = db.column(db.String(length=300), nullable=True)
    
# #     def __repr__(self):
# #         return f'User {User.name}'
