from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
VIDEO_DIR = 'detection_videos'  # Make sure this directory exists and contains video files

@app.route('/detection_videos')
def list_videos():
    files = [f for f in os.listdir(VIDEO_DIR) if f.endswith(('.mp4', '.avi', '.mkv'))]
    return jsonify(files)

@app.route('/detection_videos/<filename>')
def get_video(filename):
    return send_from_directory(VIDEO_DIR, filename)

def run_flask():
    print("🌐 Starting Flask server on port 5000...")
    app.run(host='0.0.0.0', port=5000)
