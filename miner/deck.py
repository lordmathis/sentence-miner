import random
import genanki

from typing import Dict, Tuple

decks: Dict[str, genanki.Deck] = {}

model = genanki.Model(
    1874360843,
    "Sentence Mining Model",
    fields=[
        {"name": "src"},
        {"name": "src_audio"},
        {"name": "target"},
        {"name": "target_audio"},
        {"name": "note"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{src}}<br>{{src_audio}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{target}}<br>{{target_audio}}',
        },
        {
            "name": "Card 2",
            "qfmt": "{{target}}<br>{{target_audio}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{src}}<br>{{src_audio}}',
        },
    ],
)


class AudioNote(genanki.Note):
    @property
    def guid(self):
        return genanki.guid_for(self.fields["src"], self.fields["target"])

def gen_deck_id():
    return random.randrange(1 << 30, 1 << 31)

def create_deck(deck_id, name) -> genanki.Deck:

    if name in decks:
        raise ValueError(f"Deck with the name {name} already exists")

    deck = genanki.Deck(deck_id, name)
    decks[name] = deck

    return deck

def get_deck(name):
    if name not in decks:
        raise ValueError(f"Deck with the name {name} does not exists")

    return decks[name]

def get_deck_names():
    return decks.keys
    
def add_note():
    pass