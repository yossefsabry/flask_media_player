import os
from urllib.parse import unquote ## for allow transmits bits over the server
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True  # Enable debug mode
# Define the upload folder inside the static directory
UPLOAD_FOLDER = 'static/videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# router for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/local-video', methods=['POST', 'GET'])
def local_video():
    if request.method == 'POST':
        uploaded_file = request.files.get('videoUpload')  # Get the uploaded file
        if uploaded_file and uploaded_file.filename:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(file_path)  # Save the uploaded file

            # Generate the correct URL for the uploaded file
            video_url = url_for('static', 
                                filename=f'uploads/{uploaded_file.filename}', _external=True)
            return render_template('localvideo.html', video_url=video_url)

        return "No file uploaded", 400  # Bad Request if no file uploaded

    # Handle GET requests (if needed)
    video_url = request.args.get('url')
    if video_url:
        video_url = unquote(video_url)

    print("Video URL:", video_url)  # Debugging
    if not video_url:
        return redirect('/')

    return render_template('localvideo.html', video_url=video_url)





@app.route('/v/')
def videoplayer():
    if not request.args.get('url'):
        return redirect('/')
    ## passing url for vidoe
    return render_template('videoplayer.html', url=request.args.get('url')) 


## for production temp
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) 
    # app.run(host='0.0.0.0', debug=True)


## for deploy
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 10000))
#     app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    app.run(debug=True)
