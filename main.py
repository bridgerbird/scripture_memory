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

    # variable to test class functions with
    verse_entry = landmark_verses.get_entry_by_verse("2 Nephi 2:25")

    # write a note and change the date_started
    changes = {"notes":"This one came easily"}
    changes["date_started"] = "2026-02-25" #started in class without the app
    changes["date_added"] = "2001-04-25" #testing protected fields
    landmark_verses.update_entry(verse_entry["id"], changes)
    landmark_verses.save()

    # record a review
    review_score = 5
    landmark_verses.record_review(verse_entry["id"],review_score)
    landmark_verses.save()

    # add first chunks
    chunks = [
        {
            "title":"Phrases",
            "chunk_list":[
                "Adam fell that men might be;",
                "and men are, that they might have joy."
            ]
        }
    ]
    chunks.append({
        "title":"Test",
        "chunk_list":[
            "Adam fell that"
        ]
    })
    landmark_verses.update_chunks(verse_entry["id"],chunks)
    landmark_verses.save()

    # delete a scripture
    to_delete = landmark_verses.get_entry_by_verse("2 Nephi 2:25")
    landmark_verses.remove(to_delete["id"])
    landmark_verses.save()
    # FIXME if temp_scripture["marked_text"] != scriptures[text], add '...' in appropriate places


    # TESTING CONCEPTS
    # create chunk defaults
    temp_scripture = landmark_verses.get_entry_by_verse("1 Nephi 1:20")
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
