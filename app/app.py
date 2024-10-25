import os

from flask import Flask
from loaders import load_page
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def health():
    return 'Web Loader is running!'

@app.route('/load/<path:url>')
def load_url(url):
    try:
        page_data = load_page(url)
        return jsonify(page_data), 200
    except Exception as e:
        return jsonify({"error": "Failed to load page", "details": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("LISTENER_PORT"))