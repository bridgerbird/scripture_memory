"""Loads access to the Scriptures"""
import json

scripture_file = "data/lds-scriptures-canon.json"

class ScriptureLoader:
    def __init__(self, file=scripture_file):
        with open(scripture_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Flat list for iteration
        self._scriptures = data
        # Dictionary index for fast lookups by verse title
        self._index = {verse["verse_title"]: verse for verse in data}
