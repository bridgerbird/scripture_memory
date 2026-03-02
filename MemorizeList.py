"""Represents a single memorization list and manages its data"""
import json
import uuid
from datetime import date

class MemorizeList:
    """Class for Memorize Lists"""
    def __init__(self, name: str, file: str):
        # sets name, path, loads data from file
        self.name = name
        self.file = file
        self.entries = self._load()

    #-------------------------------------
    # File I/O
    #-------------------------------------
    def _load(self) -> list:
        """Reads from file, returns list"""
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return [] # Memorize list has nothing added yet

    def save(self):
        """Writes current entries to file"""
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, indent=4)

    #-------------------------------------
    # Entry Management
    #-------------------------------------
    def add(self, entry):
        """Adds a new entry to the Memorize List"""
        today = date.today().isoformat()

        data = {
            "id": str(uuid.uuid4()),
            "date_added": today,
            "date_started": today,
            "last_reviewed": None,
            "mastery_score": 0,
            "mastery_score_history": [],
            "notes": "",
            "verse_titles": entry["verse_titles"],
            "marked_text": entry["marked_text"],
            "chunks": []
        }

        self.entries.append(data)

    def remove(self, id):
        # removes entry by id
        pass

    def get_entry(self, id):
        # returns a single entry
        pass

    def update_entry(self, id, changes):
        # edits fields on an existing entry
        pass