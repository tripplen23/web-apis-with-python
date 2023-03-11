# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will 
    1. Provide usage instructions formatted as JSON
    """
    response={"usage":"/dict=<word>"}
    return jsonify(response)


@app.get("/dict")
def dictionary():
    """
    DICT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get('word')

    # Return a error of unvalid word
    if not word:
        return jsonify({"status": "error","data": "Not a valid word or no word provided"})
    
    # Try to find exact match
    definitions = match_exact(word)
    # Nếu definition match chính xác 1 data bên trong db => trả về definition là data
    if definitions:
        return jsonify({"status": "success", "data":definitions})
    
    # Try to find an approoriate match
    definitions = match_like(word)
    if definitions:
        return jsonify({"status": "partial", "data":definitions})
    else:
        return jsonify({"status": "error", "data": "Word not found"})

if __name__ == "__main__":
    app.run()
