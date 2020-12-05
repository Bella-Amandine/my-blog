from . import db
from datetime import datetime

class Writer(db.Model):
    '''
    Writer class to create a writer model
    '''

    __tablename__ = 'writers'

    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(255)) 
    email = db.Column(db.String(255), unique = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'writer', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.email}'

class Blog(db.Model):
    '''
    Blog class to create a blog model
    '''

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    blog_message = db.Column(db.String(255))
    blog_pic_path = db.Column(db.String(255))
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = "dynamic")


    def __repr__(self):
        return f'User {self.blog_message}'

class Comment(db.Model):
    '''
    Comment class to create a comment model
    '''

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment_message = db.Column(db.String(255))
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'User {self.comment_message}'
