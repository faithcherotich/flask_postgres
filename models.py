from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Music(db.Model):
    __tablename__='music'
    
    id = db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String)
    artist= db.Column(db.String)
    album_image=db.Column(db.Text)
    # album_link= db.Column(db.Text)


    