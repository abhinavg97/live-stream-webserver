import os
import time
from flask import Flask, send_from_directory, Response, render_template
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__, template_folder='./templates')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Serve the HTML player."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)