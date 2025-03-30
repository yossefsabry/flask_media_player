import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB limit
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'webm'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/v/')
def videoplayer():
    url = request.args.get('url')
    if not url:
        return redirect('/')
    return render_template('videoplayer.html', url=url)


@app.route('/local-video/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'video' not in request.files:
            return 'No video part'
        file = request.files['video']
        if file.filename == '':
            return 'No selected video'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # pyright: ignore
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('local_video', uploaded_video=filename))
        else:
            return "Invalid file type. Allowed types are mp4, avi, mov, webm."
    return render_template('index.html', uploaded_video=None)


@app.route('/local-video')
def local_video():
    uploaded_video = request.args.get('uploaded_video')
    return render_template('localvideo.html', uploaded_video=uploaded_video)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
