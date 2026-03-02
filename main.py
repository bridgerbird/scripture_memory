# lds-scriptures-json.txt comes from Nephi.org

from ScriptureLoader import ScriptureLoader
from MemorizeList import MemorizeList

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
    to_delete = landmark_verses.get_entry_by_verse("2 Nephi 2:25")
    landmark_verses.remove(to_delete["id"])
    landmark_verses.save()
    # FIXME if temp_scripture["marked_text"] != scriptures[text], add '...' in appropriate places


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
