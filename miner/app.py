from flask import Flask, render_template, request
from miner.deck import create_deck, get_deck_names, gen_rand_deck_id
from miner.translate import get_translate_languages

app = Flask(__name__)

@app.route("/")
def index():
    deck_list = get_deck_names()
    return render_template("index.html", deck_list=deck_list)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':

        languages = get_translate_languages()
        return render_template("create.html", languages=languages)
    
    try:
        deck_id = gen_rand_deck_id()

        deck_name = request.form.get("deck-name")
        src_lang = request.form.get("source-lang")
        target_lang = request.form.get("target-lang")

        deck = create_deck(deck_id, deck_name, src_lang, target_lang)        
        return deck.to_json()
        
    except ValueError as e:
        return "Deck name exists", 400

@app.route("/edit")
def edit():
    pass
   

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, debug=True)