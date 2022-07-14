#  Created by Sofiia Tesliuk at 2019-09-29.
from flask import Flask, render_template, request, send_file

from image import ImageProcessor

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if ImageProcessor.valid_format(image.filename):
                if 'ico' in request.form:
                    result_icon, icon_filename = ImageProcessor.create_ico(image)
                    return send_file(result_icon,
                                     as_attachment=True,
                                     attachment_filename=icon_filename)
                elif 'icns' in request.form:
                    result_icon, icon_filename = ImageProcessor.create_icns(image)
                    return send_file(result_icon,
                                     as_attachment=True,
                                     attachment_filename=icon_filename)
                else:
                    error = 'Icon format is not selected.'
                    return render_template('upload.html', error=error)

            else:
                error = 'Invalid image format.'
                if image.filename == '':
                    error = 'Image is not selected.'
                return render_template('upload.html', error=error)
    return render_template('upload.html', error=False)


@app.errorhandler(400)
def icon_not_found(error):
    return render_template('error.html', error=error, error_number=400), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error, error_number=404), 404


if __name__ == '__main__':
    app.run(debug=True)
