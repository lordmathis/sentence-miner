from flask import Flask, render_template, request
from deck import create_deck

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("create.html")
    
    return create_deck()

@app.route("/edit")
def edit():
    pass
    

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, debug=True)