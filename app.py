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
    response={ "usage":"/dict?=<word>" }
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
    words = request.args.getlist('word')

    # Return a error of unvalid word
    if not words:
        response = ({"status":"error", "word":words, "data":"Not a valid word or no word provided"})
        return jsonify(response)
    
    # Initialize the response
    response = {"words":[]}

    for word in words:
        # Try to find an exact match
        definitions = match_exact(word)

        # Nếu definition match chính xác 1 data bên trong db => trả về definition là data
        if definitions:
            response["words"].append({ "status":"success", "word":word, "data":definitions })
        else:
            # Try to find an approoriate match
            definitions = match_like(word)

            if definitions:
                response["words"].append({"status":"partial", "word":word, "data":definitions})
            else:
                response["words"].append({"status":"error", "word":word, "data":"Word not found"})

    #Return the response after processing all words:
    return jsonify(response)

if __name__ == "__main__":
    app.run()

"""
Algorithm for checking the list of words in the declaration
1. For each word in the list of words
    1. Search for an exact match
    2. If an exact match is found: append the data in response
    3. If an exact match is not found
        1. Search for an approx. match
        2. If an approx. match is found: append the data in response
        3. If approx. match is not found: Add error in the response
2. Return the final response
"""