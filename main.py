from flask import Flask, render_template
import os
url = 'https://apod.nasa.gov/apod/image/2210/CannonSupernova_English_8404.jpg'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/result')
def result_page():
    return render_template('result.html')
@app.route('/magic')
def magic_page():
    from deepdream import run
    run()
    return render_template('magic.html')

if __name__ == "__main__":
    app.run(debug=True)