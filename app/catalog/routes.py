from app.catalog import main
from app import db
from app.catalog.models import Song, Publication
from flask import render_template, request, redirect, url_for, flash
from app.catalog.forms import EditMusicForm, CreateMusicForm
from flask_login import login_required


@main.route('/')
def display_songs():
    songs=Song.query.all()
    return render_template('home.html',songs=songs)
@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_songs = Song.query.filter_by(pub_id = publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_songs=publisher_songs)

@main.route('/song/delete/<song_id>', methods=['GET', 'POST'])
@login_required
def delete_song(song_id):
    song = Song.query.get(song_id)
    if request.method == 'POST':
        db.session.delete(song)
        db.session.commit()
        flash('Song deleted successfully')
        return redirect(url_for('main.display_songs'))
    return render_template('delete_book.html', song=song, song_id=song.id)

@main.route('/edit/song/<song_id>', methods=['GET', 'POST'])
@login_required
def edit_song(song_id):
    song = Song.query.get(song_id)
    form = EditMusicForm(obj=song)
    if form.validate_on_submit():
        song.title = form.title.data
        song.song_lyricist = form.song_lyricist.data
        song.music_director = form.music_director.data
        db.session.add(song)
        db.session.commit()
        flash('Song Edited Successfully')
        return redirect(url_for('main.display_songs'))
    return render_template('edit_book.html', form=form)


@main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
@login_required
def create_song(pub_id):
    form = CreateMusicForm()
    form.pub_id.data = pub_id  # pre-populates pub_id
    if form.validate_on_submit():
        song = Song(title=form.title.data, singers=form.singers.data, avg_rating=form.avg_rating.data,
                    song_lyricist=form.song_lyricist.data, image=form.img_url.data, music_director=form.music_director.data,
                    pub_id=form.pub_id.data)
        db.session.add(song)
        db.session.commit()
        flash('Song added successfully')
        return redirect(url_for('main.display_publisher', publisher_id=pub_id))
    return render_template('create_book.html', form=form, pub_id=pub_id)