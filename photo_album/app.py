from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    photos = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', photos=photos)

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['photo']
    if photo:
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))
    return redirect('/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
