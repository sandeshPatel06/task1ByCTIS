from flask import Flask, request, render_template, send_file, jsonify
from gtts import gTTS
import os
from io import BytesIO

app = Flask(__name__)

# Supported languages and their codes
languages = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'hi': 'Hindi'
}

@app.route('/')
def index():
    # Render the index.html template and pass the languages dictionary to it
    return render_template('index.html', languages=languages)

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    # Retrieve the form data
    text = request.form['text']
    language = request.form['language']

    # Initialize the Google Text-to-Speech engine
    tts = gTTS(text=text, lang=language)
    
    # Save the speech to a BytesIO object
    audio = BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)  # Go to the start of the BytesIO object

    # Send the generated MP3 file as a response to the client
    return send_file(audio, as_attachment=True, download_name='output.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    # Run the Flask application 
    app.run(debug=False)
