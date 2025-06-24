from flask import Flask, render_template, request
from detect import detect_living_beings
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_url = None
    if request.method == 'POST':
        file = request.files['image']
        path = f'static/uploads/{file.filename}'
        file.save(path)
        result, image_url = detect_living_beings(path)
    return render_template('index.html', result=result, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
