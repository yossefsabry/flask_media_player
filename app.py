from urllib.parse import unquote ## for allow transmits bits over the server
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config["DEBUG"] = True  # Enable debug mode

# router for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/local-video')
def local_video():
    video_url = request.args.get('url') ## check for url param
    if video_url:
        video_url = unquote(video_url)
    print("Video URL:", video_url) # debuger
    if not video_url:
        return redirect('/')
    return render_template('localvideo.html', video_url=video_url)

@app.route('/v/')
def videoplayer():
    if not request.args.get('url'):
        return redirect('/')
    ## passing url for vidoe
    return render_template('videoplayer.html', url=request.args.get('url')) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) 

