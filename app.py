import os
import sys
import uuid
from flask import Flask, render_template
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__, template_folder='./templates')
CORS(app)  # Enable CORS for all routes

# Generate unique ID if not provided via command line
peer_id = sys.argv[2] if len(sys.argv) > 2 else f"peer-{uuid.uuid4()}"  # Generate UUID if no ID provided


@app.route('/')
def index():
    """Serve the default HTML player with the peer ID dynamically injected."""
    return render_template('index.html', peer_id=peer_id)


@app.route('/<template_name>')
def serve_template(template_name):
    """
    Serve a specific template file dynamically.
    """
    if not template_name.endswith('.html'):
        template_name += '.html'  # Ensure the file ends with .html

    try:
        return render_template(template_name, peer_id=peer_id)
    except Exception as e:
        return f"Error loading template '{template_name}': {str(e)}", 404


if __name__ == '__main__':
    app.run(debug=True, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)  # Default to port 8000 if not specified
