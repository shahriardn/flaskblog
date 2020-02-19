import os
import random

from flask import request
# from routes import app
from flask_login import current_user
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def uploadfile(request,app):
    try:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                if not os.path.exists(
                    os.path.join(
                        app.root_path,
                        app.config['STATIC_FOLDER'],
                        'images/{username}'
                        .format(
                            username=str(current_user.username)
                        )
                    )
                ):
                    os.mkdir(
                        os.path.join(
                            app.root_path,
                            app.config['STATIC_FOLDER'],
                            'images/{username}'
                            .format(username=str(current_user.username)
                                    )
                        )
                    )
                filenamefinal = str(random.randint(0, 999)) + '.' + filename
                file.save(os.path.join(app.root_path,
                                       app.config['STATIC_FOLDER'], 'images/{username}'.format(username=str(current_user.username)), filenamefinal))
                # return redirect(url_for('uploaded_file',
                # filename=filename))

        return filenamefinal

    except Exception as error:
        print('errrrrrrrrrrrrrrrrrrrrrrror',error)
        return {"error": error}
