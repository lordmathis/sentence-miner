from flask import Flask, render_template, request
from deck import create_deck, get_deck_names, gen_rand_deck_id

app = Flask(__name__)

@app.route("/")
def index():
    deck_list = list_deck_names()
    return render_template("index.html", deck_list)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("create.html")
    
    try:
        deck_name = request.form.get()
        deck_id = gen_rand_deck_id()

        deck = create_deck(deck_id, deck_name)        
        return deck.to_json()
        
    except ValueError as e:
        return "Deck name exists", 400

@app.route("/edit")
def edit():
    pass

@app.route("/list")
def list_deck_names():
    return get_deck_names
    

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, debug=True)