from . import db

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

