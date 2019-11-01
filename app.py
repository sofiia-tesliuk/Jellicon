#  Created by Sofiia Tesliuk at 2019-09-29.
import os

from werkzeug.exceptions import NotFound
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, after_this_request

from image import UnImage

app = Flask(__name__)

STORAGE_DIRECTORY = "icons"


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if UnImage.valid_format(image.filename):
                icon_filename = UnImage.create_ico(STORAGE_DIRECTORY, image)
                return render_template('download.html', icon_filename=icon_filename)
            else:
                error = 'Invalid image format.'
                if image.filename == '':
                    error = 'Image is not selected.'
                return render_template('upload.html', error=error)
    return render_template('upload.html', error=False)


@app.route('/download/<icon_filename>')
def download_icon(icon_filename):
    try:
        @after_this_request
        def cleanup(response):
            try:
                os.remove('{}/{}'.format(STORAGE_DIRECTORY, icon_filename))
            except FileNotFoundError:
                return response
            return response

        return send_from_directory(STORAGE_DIRECTORY, icon_filename, as_attachment=True)
    except (KeyError, NotFound):
        return redirect(url_for('upload_image'))


@app.errorhandler(400)
def icon_not_found(error):
    return render_template('error.html', error='400: Icon not found.'), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error='404: Page or icon not found.'), 404


if __name__ == '__main__':
    app.run(debug=True)
