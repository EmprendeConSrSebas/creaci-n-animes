from flask import Flask, request, jsonify, send_file
import os
import requests
import subprocess

app = Flask(__name__)

# Función para generar imágenes con DALL·E
def generate_image(prompt):
    api_url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    data = {"prompt": prompt, "n": 1, "size": "1024x1024"}
    response = requests.post(api_url, headers=headers, json=data)
    img_url = response.json()["data"][0]["url"]
    img_path = "generated_image.png"
    img_data = requests.get(img_url).content
    with open(img_path, "wb") as f:
        f.write(img_data)
    return img_path

# Función para generar voz con Google TTS
def generate_audio(text):
    from gtts import gTTS
    tts = gTTS(text, lang="es")
    audio_path = "narration.mp3"
    tts.save(audio_path)
    return audio_path

# Función para componer el video con FFmpeg
def create_video(image_path, audio_path, output_path):
    cmd = [
        "ffmpeg", "-loop", "1", "-i", image_path, "-i", audio_path,
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac",
        "-b:a", "192k", "-shortest", "-vf", "scale=1280:720", output_path
    ]
    subprocess.run(cmd)
    return output_path

@app.route("/generate_video", methods=["POST"])
def generate_video():
    data = request.get_json()
    text = data.get("text", "")

    # Generar imagen y audio
    image_path = generate_image(text)
    audio_path = generate_audio(text)

    # Crear video final
    video_path = "output.mp4"
    create_video(image_path, audio_path, video_path)

    return jsonify({"video_url": "/download_video"})

@app.route("/download_video")
def download_video():
    return send_file("output.mp4", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
