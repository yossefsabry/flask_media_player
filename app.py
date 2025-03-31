
### Flask Video Player
### A simple web application that allows users to upload and play videos.
### and watch youtube videos and record and play videos from webcam.
### The application is built using Flask, a Python web framework.
### port: 10000
# ========================================================
#### references
# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/#uploading-files
# https://github.com/jechav/flask-video-player
# ========================================================

import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads' # folder where uploaded videos are stored
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # set the upload folder
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB limit
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'webm'} # allowed video file extensions
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # create the upload folder if it doesn't exist
# allow debugging in the browser for production
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def allowed_file(filename):
    """
    description: check if the file extension is allowed
    :param filename: the name of the file
    """
    # check if the file extension is allowed
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/v/')
def videoplayer():
    """
    description: play a video from a URL
    parameters:
        - url: the URL of the video 
    """
    url = request.args.get('url') # get the URL parameter
    if not url:
        return redirect('/')
    # redirect to the video player template for youtube videos
    return render_template('videoplayer.html', url=url)


# not used now i will use it later maybe
# @app.route('/local-video/<filename>')
# def uploaded_file(filename):
#     """
#     description: play an uploaded video
#     parameters:
#         - filename: the name of the video file
#     """
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    description: home page of the application and upload a video
    parameters:
        - video: the video file to upload
        - uploaded_video: the name of the uploaded video
    """
    if request.method == 'POST': # check if the request method is POST
        if 'video' not in request.files: # check if the video part is in the request
            return 'No video part'
        file = request.files['video']
        if file.filename == '': # check if the file name is empty
            return 'No selected video'
        if file and allowed_file(file.filename): # check if the file is allowed
            # secure the file to save from path (traversal attacks)
            filename = secure_filename(file.filename) # pyright: ignore
            # save the file to the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # redirect to the uploaded video
            return redirect(url_for('local_video', uploaded_video=filename))
        else:
            # return an error message if the file type is not allowed
            return "Invalid file type. Allowed types are mp4, avi, mov, webm."
    # render the home page template
    return render_template('index.html', uploaded_video=None)


@app.route('/local-video')
def local_video():
    """ 
    description: play the uploaded video
    parameters:
        - uploaded_video: the name of the uploaded video
    """
    # get the name of the uploaded video
    uploaded_video = request.args.get('uploaded_video')
    # render the local video template
    return render_template('localvideo.html', uploaded_video=uploaded_video)


# run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
