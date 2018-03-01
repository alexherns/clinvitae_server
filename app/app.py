from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from db import get_connection
from models import searchVariants, autocompleteGenes

app = Flask(__name__)
CORS(app)

@app.route("/genes/suggestions")
def suggest():
    prefix = request.args.get('prefix')
    c = get_connection().cursor()
    genes = autocompleteGenes(c, prefix)
    return jsonify({
        "results": genes,
    })

@app.route("/variants")
def search():
    gene = request.args.get('gene')
    c = get_connection().cursor()
    variants = searchVariants(c, gene=gene)
    return jsonify({
        "results": variants,
    })
