from os import getenv
from flask import Flask, jsonify

LISTEN_PORT = getenv("LISTEN_PORT", 8000)
DB_HOSTNAME = getenv("DB_HOSTNAME", "db")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Hello world",
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=LISTEN_PORT)

