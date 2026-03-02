# lds-scriptures-json.txt comes from Nephi.org

from ScriptureLoader import ScriptureLoader
from MemorizeList import MemorizeList

# def load_memorize_list(file):
#     """Return a memorize list object from the included file"""
#     try:
#         with open(file, "r", encoding='utf-8') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return [] #Memorize list has nothing added yet

# def add(entry, memorize_list):
#     """Adds an entry to a memorize list"""
#     today = date.today().isoformat()

#     data = {
#         "id": str(uuid.uuid4()),
#         "date_added": today,
#         "date_started": today,
#         "last_reviewed": today,
#         "mastery_score": 0,
#         "mastery_score_history": [],
#         "notes": "",
#         "verse_titles": entry["verse_titles"],
#         "marked_text": entry["marked_text"],
#         "chunks": []
#     }

#     memorize_list.append(data)
#     return memorize_list

# def save(memorize_list, file):
#     """Saves the newly added entry to file"""
#     with open(file, "w") as f:
#         json.dump(memorize_list, f, indent=4)

def main():
    """Main driver"""
    # Load the canon scriptures
    scriptures = ScriptureLoader()
    # Examples of using ScriptureLoader()
    example_verse = scriptures.get_verse("1 Nephi 3:7")

    # Load users Landmark Verses
    landmark_verses = MemorizeList("bridgers_landmarks", "data/user-lists/bridgers-landmarks.json")

    # ==========================================================
    # TESTING CONCEPTS
    # add a scripture
    marked_verse_1 = {
        "list_name":"landmark_verses",
        "verse_titles":[
            "2 Nephi 2:25"
        ],
        "marked_text":"Adam fell that men might be; and men are, that they might have joy.",
    }

    landmark_verses.add(marked_verse_1)
    landmark_verses.save()
    print()
    # FIXME if temp_scripture["marked_text"] != scriptures[text], add '...' in appropriate places

    # save(landmark_verses, 'bridgers-landmarks.json')

    # TESTING CONCEPTS
    # create chunk defaults
    temp_scripture = landmark_verses[0]
    temp_scripture["text_alterations"] = {
        "every_other":None,
        "first_three":None
    }


    # Take the text and save some different options
    words = temp_scripture["marked_text"].split()

    # Every other word replaced with '___'
    every_other_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            every_other_words.append(word)
        else:
            every_other_words.append("___")
    temp_scripture["text_alterations"]["every_other"] = " ".join(every_other_words)

    # First 3 words only
    temp_scripture["text_alterations"]["first_three"] = " ".join(words[:3])
    # FIXME if first 3 words are "And it came", add 5 more words. That will help with verses that start with "And it came to pass"

    print(
        f"FULL Scripture\n"
        f"Source: FIXME: get volume_title from lds-scriptures-json by matching 1st element in vers_titles from landmarks to verse title from lds-scriptures\n"
        f"Reference: {temp_scripture['verse_titles']}\n"
        f"{temp_scripture['marked_text']}\n\n"
    )

    print(
        f"Scripture 50%\n"
        f"Reference: {temp_scripture['verse_titles']}\n"
        f"{temp_scripture['text_alterations']['every_other']}\n\n"
    )

    print(
        f"REFERENCE AND 3\n"
        f"Reference: {temp_scripture['verse_titles']}\n"
        f"{temp_scripture['text_alterations']['first_three']}\n"
    )

if __name__ == "__main__":
    main()
