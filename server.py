from flask import Flask, request, jsonify, send_from_directory
import os
from gtts import gTTS
import ffmpeg

app = Flask(__name__)

OUTPUT_FOLDER = "videos"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/generate", methods=["POST"])
def generate_video():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Texto vacío"}), 400

    audio_path = os.path.join(OUTPUT_FOLDER, "audio.mp3")
    video_path = os.path.join(OUTPUT_FOLDER, "output.mp4")
    image_path = "anime_background.jpg"  # Imagen base

    # Generar voz con gTTS
    tts = gTTS(text, lang="es")
    tts.save(audio_path)

    # Generar video con FFMPEG
    ffmpeg.input(image_path, loop=1, t=10).output(video_path, vf="scale=1280:720", **{"c:v": "libx264"}, r=30, an=None).run(overwrite_output=True)
    ffmpeg.input(video_path).input(audio_path).output(video_path, vcodec="copy", acodec="aac").run(overwrite_output=True)

    return jsonify({"video": video_path})

@app.route("/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
