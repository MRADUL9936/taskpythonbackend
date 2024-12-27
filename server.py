
from flask import Flask,request, render_template
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # The HTML form

@app.route('/upload', methods=['POST'])
def upload_file():
    
    return 'Sucessefull response', 200


if __name__ == '__main__':
    app.run(debug=True)
