from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os
import datetime

app = Flask(__name__)

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file:
        new_file = os.path.join('./uploads', generate_unique_filename(file.filename))
        file.save(new_file)
        text = extract_text(new_file)
        return render_template('result.html', text=text)

def generate_unique_filename(filename):
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d%H%M%S%f') + '_' + filename

def extract_text(image):
    # Set Tesseract language configuration
    text = pytesseract.image_to_string(Image.open(image), config='-l jpn+eng')
    return text

if __name__ == '__main__':
    app.run(debug=True)
