# build the Flask app here

from flask import Flask, render_template, request, redirect, url_for
from main import rec_albums, rec_songs, get_relatedArtists, get_artistID

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

@app.route('/songs/<artistID>')
def songs(artistID=None):
    if artistID:
        dict_songs = rec_songs(get_relatedArtists(artistID))
        return render_template('song-result.html', output=dict_songs)
    return redirect(url_for('/'))

@app.route('/albums/<artistID>')
def albums(artistID=None):
    if artistID:
        dict_albums = rec_albums(get_relatedArtists(artistID))
        return render_template('album-result.html', output=dict_albums)
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