from flask import Flask, redirect, render_template, request
from miner.deck import create_deck, get_deck, get_decks, gen_rand_deck_id
from miner.translate import get_translate_languages

app = Flask(__name__)

@app.route("/")
def index():
    decks = get_decks()
    return render_template("index.html", decks=decks)

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
        return redirect(f"/edit?deck-id={deck.deck_id}")
        # return render_template("edit.html", selected_deck=deck.name)
        
    except ValueError:
        return "Deck name exists", 400

@app.route("/edit")
def edit():

    try:
        deck_id = int(request.args.get('deck-id'))
    except ValueError:
        return "Deck id required", 400

    try:
        deck = get_deck(deck_id)
        return render_template("edit.html", deck_name=deck.name, deck_id=deck.deck_id)

    except ValueError:
        return "Deck not found", 404

@app.route("/add", methods=["POST"])
def add():

    try:
        deck_id = int(request.args.get('deck-id'))
    except ValueError:
        return "Deck id required", 400
    
    try:
        deck = get_deck(deck_id)

        front = request.form.get("front")
        back = request.form.get("back")

        deck.add_note(front, back)

        return render_template("note.html", front=front, back=back)

    except ValueError:
        return "Deck not found", 404

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, debug=True)