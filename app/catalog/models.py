from app import db
from datetime import datetime

# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'The Publisher is {}'.format(self.name)


# SONGS TABLE
class Song(db.Model):
    __tablename__ = 'song'


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    singers = db.Column(db.String(600))
    avg_rating = db.Column(db.Float)
    song_lyricist = db.Column(db.String(400))
    image = db.Column(db.String(100), unique=True)
    music_director = db.Column(db.String(400))
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH RELATIONSHIP
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, singers, avg_rating, song_lyricist, image, music_director, pub_id):

        self.title = title
        self.singers = singers
        self.avg_rating = avg_rating
        self.song_lyricists = song_lyricist
        self.image = image
        self.music_director = music_director
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.singers)

