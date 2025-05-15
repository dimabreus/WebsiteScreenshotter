from urllib.parse import urlparse

from flask import Flask, request
from flask_cors import CORS

from src.screenshot import take_screenshot as take_screen

app = Flask(__name__)
CORS(app)


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


@app.route("/take_screenshot", methods=['POST'])
def take_screenshot():
    body = request.json
    website_url = body.get('website')

    if not website_url:
        return {
            'code': 400,
            'message': 'Website URL is required'
        }, 400

    if not is_valid_url(website_url):
        return {
            'code': 400,
            'message': 'Invalid website URL'
        }, 400

    data = take_screen(website_url)

    return {
        'code': 200,
        'message': 'OK',
        'data': data
    }


if __name__ == "__main__":
    app.run(port=8800, debug=True)
