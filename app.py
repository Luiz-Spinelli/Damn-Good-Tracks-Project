# build the Flask app here

from flask import Flask, render_template, request
from main import rec_albums, rec_songs, get_relatedArtists, get_artistID

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def get_recs():
    if request.form.get('songs'):
        if request.method == "POST":
            artist_name = request.form["input"]
            x = get_artistID(artist_name)
            if x[0]:
                dict_songs = rec_songs(get_relatedArtists(x[1]))
                return render_template('song-result.html', output=dict_songs)
            else:
                return render_template('wrong-input.html', correct_name=x[1])
    if request.form.get('albums'):
        if request.method == "POST":
            artist_name = request.form["input"]
            x = get_artistID(artist_name)
            if x[0]:
                dict_albums = rec_albums(get_relatedArtists(x[1]))
                return render_template('album-result.html', output=dict_albums)
            else:
                return render_template('wrong-input.html', correct_name=x[1])   

    return render_template('form.html') 

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