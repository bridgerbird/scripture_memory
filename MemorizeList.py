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

    def remove(self, entry_id: str) -> bool:
        """Removes an entry by id
           Returns True if found and removed, False if id not found."""
        original_count = len(self.entries)
        self.entries = [e for e in self.entries if e["id"] != entry_id]
        return len(self.entries) < original_count

    def get_entry(self, entry_id: str) -> dict | None:
        """Returns a single entry found by id"""
        for entry in self.entries:
            if entry["id"] == entry_id:
                return entry
        return None

    def get_entry_by_verse(self, verse_title: str) -> dict | None:
        """Find an entry by verse"""
        for entry in self.entries:
            if verse_title in entry["verse_titles"]:
                return entry
        return None

    def update_entry(self, id, changes):
        # edits fields on an existing entry
        pass
