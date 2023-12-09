from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
