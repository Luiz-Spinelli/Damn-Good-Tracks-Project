# build the Flask app here

from flask import Flask, render_template, request, redirect, url_for
from main import get_artist, rec_albums, rec_songs, get_relatedArtists, get_artistID
import urllib.request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def get_recs():
    if request.method == "POST":
        artist_name = request.form["input"]
        x = get_artistID(artist_name)
        if x[0]:
            if request.form.get('songs'):
                return redirect(url_for('songs', artistID=x[1]))
            elif request.form.get('albums'):
                return redirect(url_for('albums', artistID=x[1]))
        else:  # case that input is not accurate
            return render_template('wrong-input.html', correct_name=x[1])    

    return render_template('form.html') 

@app.route('/songs/<artistID>', methods=["GET", "POST"])
def songs(artistID=None):
    if artistID:
        dict_songs = rec_songs(get_relatedArtists(artistID))
        artist_name = get_artist(artistID)['name']
        artist_img = get_artist(artistID)['images'][1]['url']
        return render_template('song-result.html', output=dict_songs, name=artist_name, img=artist_img)
    if request.method == "POST":
        if request.form.get('shuffle'):
            return redirect(url_for('songs', artistID=artistID))
    return redirect(url_for('/'))

@app.route('/albums/<artistID>', methods=["GET", "POST"])
def albums(artistID=None):
    if artistID:
        dict_albums = rec_albums(get_relatedArtists(artistID))
        artist_name = get_artist(artistID)['name']
        artist_img = get_artist(artistID)['images'][1]['url']
        return render_template('album-result.html', output=dict_albums, name=artist_name, img=artist_img)
    if request.method == "POST":
        if request.form.get('shuffle'):
            return redirect(url_for('albums', artistID=artistID))
    return redirect(url_for('/'))

# # if website domain is www.abc.com, http://www.abc.com/ will triger the function below, hello()
# @app.route('/hello/<name>')
# # if the route contains /hello/name, it will triger the function below, hello(name)
# def hello(name=None):
#     if name:
#         # return f'<h1>Hello, {name}!</h1><p>I am excited to learn flask.</p>'
#         return render_template('hello.html', username=name)
#     return '<h1>Hello, world!</h1>'

if __name__ == "__main__":
    app.run(debug=True)