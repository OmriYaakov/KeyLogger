from flask import Flask, request
import os

app = Flask(__name__)

# Directory to store uploaded log files
upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    filepath = os.path.join(upload_dir, file.filename)
    file.save(filepath)
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
