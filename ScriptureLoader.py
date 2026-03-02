"""Loads access to the Scriptures"""
import json

SCRIPTURE_FILE = "data/lds-scriptures-canon.json"

class ScriptureLoader:
    """Creates Scriptures object"""
    def __init__(self, file=SCRIPTURE_FILE):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Flat list for iteration
        self._scriptures = data
        # Dictionary index for fast lookups by verse title
        self._index = {verse["verse_title"]: verse for verse in data}

    def get_verse(self, title: str) -> dict | None:
        """Look up a verse by its scriptural reference, e.g. '1 Nephi 3:7' """
        return self._index.get(title)

    def get_chapter(self, book_title: str, chapter_number: int) -> list:
        """Return all verses in a given chapter"""
        return [
            v for v in self._scriptures
            if v["book_title"] == book_title
            and v["chapter_number"] == chapter_number
        ]
