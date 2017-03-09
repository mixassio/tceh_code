from sqlalchemy_utils import EmailType
from app import db
from sqlalchemy import MetaData

metadata = MetaData()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(EmailType, nullable=False)
    postes = db.relationship('Post', backref='user', lazy='dynamic')


class Tags(db.Model):
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.Unicode, nullable=False)
    is_visible = db.Column(db.Boolean, nullable=False)
    slug = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.relationship('Tag', secondary='tags', backref=db.backref('posts', lazy='dynamic'))
    users = db.relationship('User', backref='post')

    def __init__(self, title, content, is_visible, user_id):
        self.title = title
        self.content = content
        self.is_visible = is_visible
        self.slug = self.title.replace(' ', '-')
        self.user_id = user_id


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
