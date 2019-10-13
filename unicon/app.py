#  Created by Sofiia Tesliuk at 2019-09-29.
from unicon.image import UnImage

from flask import Flask, render_template, request, redirect, send_from_directory, abort

app = Flask(__name__)

STORAGE_DIRECTORY = "icons"

downloaded_icons = []


@app.route('/')
def entry_point():
    return redirect('/upload')


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if UnImage.valid_format(image.filename):
                icon_filename = UnImage.create_icon(STORAGE_DIRECTORY, image)
                return render_template('download.html', icon_filename=icon_filename)
            else:
                error = 'Invalid image format.'
                return render_template('upload.html', error=error)
    return render_template('upload.html', error=None)


@app.route('/download/<icon_filename>')
def download_icon(icon_filename):
    try:
        downloaded_icons.append(icon_filename)
        return send_from_directory(STORAGE_DIRECTORY, icon_filename, as_attachment=True)
    except KeyError:
        abort(400)


@app.errorhandler(400)
def icon_not_found(error):
    return render_template('error.html', error='400: Icon not found.'), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error='404: Page not found.'), 404


if __name__ == '__main__':
    app.run(debug=True)
