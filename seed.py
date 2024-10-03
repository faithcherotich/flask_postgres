from models import Music, db
from app import app

with app.app_context():
    music1 = Music(title="test",artist="testing",album_image="testing",album_link="testing")
    music2 = Music(title="test2",artist="testing",album_image="testing",album_link="testing")
    
    db.session.add(music1)
    db.session.add(music2)
    
    db.session.commit()
     
    