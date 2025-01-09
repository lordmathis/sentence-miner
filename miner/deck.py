import genanki

from typing import Dict

decks: Dict[int, genanki.Deck] = {}

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


def create_deck(deck_id, name):
    deck = genanki.Deck(deck_id, name)
    decks[deck_id] = deck

def add_note():
    pass