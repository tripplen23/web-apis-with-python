# Import the redirect() method from "flask" library to enable us to redirect to another URL
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    #Render the index.html template and return it
    return render_template("index.html")
# TODO: Define the login of the route "/search", that will be used to listen and response to GET requests
@app.get("/search")
def search():
    #parse the arguments "q" from the incoming GET request querystring
    args = request.args.get("q")
    #redirect to Google website with the querystring of Google search and adding the argument we defined above
    return redirect(f"https://www.google.com/search?q= {args} " )
if __name__ == "__main__":
    app.run()