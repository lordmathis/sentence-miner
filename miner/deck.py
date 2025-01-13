import random
import genanki

from typing import Dict, List


class Deck:

    anki_deck: genanki.Deck
    src_lang: str
    target_lang: str

    def __init__(self, deck_id, name, src_lang, target_lang):
        self.anki_deck = genanki.Deck(deck_id, name)

        self.src_lang = src_lang
        self.target_lang = target_lang
    
    @property
    def name(self):
        return self.anki_deck.name
    
    @property
    def deck_id(self):
        return self.anki_deck.deck_id


_decks: Dict[int, Deck] = {}

_model = genanki.Model(
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


def gen_rand_deck_id():
    return random.randrange(1 << 30, 1 << 31)


def create_deck(deck_id, name, src_lang, target_lang) -> Deck:

    if name in _decks:
        raise ValueError(f"Deck with the name {name} already exists")

    deck = Deck(deck_id, name, src_lang, target_lang)

    _decks[deck_id] = deck

    return deck


def get_deck(deck_id) -> Deck:
    if deck_id not in _decks:
        raise ValueError(f"Deck not found")

    return _decks[deck_id]


def get_decks() -> List[Deck]:
    return list(_decks.values())


def add_note():
    pass
