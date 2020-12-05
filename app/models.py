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

    def __repr__(self):
        return f'User {self.blog_message}'

