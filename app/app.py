from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/genes/suggestions")
def suggest():
    prefix = request.args.get('prefix')
    return jsonify({
        "results": [prefix, prefix+'a', prefix+'b'],
    })

@app.route("/variants")
def search():
    return jsonify({
        "results": [{
            "name": "abcd",
            "effects": [1, 2, 3],
        }],
    })
