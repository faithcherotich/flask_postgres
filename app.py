from flask import Flask
from models import Music, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://osir:12345@localhost/song'
db.init_app(app)
migrate = Migrate(app,db)


@app.route('/')
def index():
    return "<h1>testing</h1>"

if __name__ == '__main__':
    app.run(port=5000,debug=True)