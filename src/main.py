from flask import Flask

app = Flask(__name__)

@app.route('/')
def default_path():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)