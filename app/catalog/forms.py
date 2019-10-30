from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditMusicForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    song_lyricist = StringField('Song lyricist', validators=[DataRequired()])
    music_director = StringField('Music director', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateMusicForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    singers = StringField('Singers', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    song_lyricist = StringField('Song Lyricist', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    music_director = StringField('Music director', validators=[DataRequired()])
    pub_id = IntegerField('PublisherID', validators=[DataRequired()])
    submit = SubmitField('Create')