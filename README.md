# Flask Video Player
A simple video player web application built using Flask, Jinja2, Bootstrap, and FontAwesome. This application allows users to stream local and online videos, including YouTube links.

# Features
- Play local videos by providing a URL.
- Supports YouTube video embedding.
- Responsive design using Bootstrap.
- FontAwesome icons for a better UI experience.
- Uses CDN for styles and scripts.

## Technologies Used
- **Flask**: A lightweight Python web framework.
- **Jinja2**: Templating engine for rendering dynamic HTML.
- **Bootstrap**: Provides a responsive UI.
- **FontAwesome**: Adds icons to the UI.
- **Video.js**: Enhances the video playback experience.

# Installation
## Clone the repository:
```sh
git clone https://github.com/yourusername/flask-video-player.git
cd flask-video-player
```

## 2.Install dependencies:
```bash
pip install -r requirements.txt
```

## 3.run flask application
```bash
python app.py
# http://127.0.0.1:5000/
```

# 4.project structure jJkx
```bash
flask-video-player/
│── static/
│   ├── main.css          # Stylesheet for the application
│── templates/
│   ├── index.html        # Home page template
│   ├── localvideo.html   # Local video player template
│   ├── videoplayer.html  # Online video player template
│── app.py                # Main Flask application
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

# Usage
- Home Page (/)
Displays a form where users can enter a video URL.
- Local Video Player (/local-video?url=video_url)
Plays local videos when a valid URL is provided.
- YouTube & Online Video Player (/v/?url=video_url)
Embeds YouTube videos.
Streams MP4 videos from a given URL.

## Example URLs
    YouTube Video:
```ruby
http://127.0.0.1:5000/v/?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
    Local Video:
```ruby
http://127.0.0.1:5000/local-video?url=/static/sample.mp4 
```
