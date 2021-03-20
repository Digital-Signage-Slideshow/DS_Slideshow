from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello world'

@app.route('/slides')
def slides():
    return jsonify([
        {'title' : 'something'},
        {'title' : 'something else'}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)