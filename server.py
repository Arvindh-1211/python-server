from flask import Flask
from extractFormat import get_formats
from downloader import download as down


app = Flask(__name__)

URL = ''

@app.route('/')
def landingPage():
    return 'hello'

@app.route('/getFormats/<path:url>')
def get_url(url):
    URL = url
    return get_formats(URL)

@app.route('/download/<path:url>')
def download(url):
    URL = url
    down(URL, 'best')

if __name__ == '__main__':
    app.run(debug = True)