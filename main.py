# lds-scriptures-json.txt comes from Nephi.org
import json

def load_scriptures(file):
    """Return a scriptures object from the included file"""
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    """Main driver"""
    # Load the canon scriptures
    scriptures = load_scriptures('lds-scriptures-json.txt')

    # Load users Landmark Verses
    landmark_verses = load_scriptures('bridgers-landmarks.txt')

    # ==========================================================
    # TESTING CONCEPTS
    temp_scripture = landmark_verses[0]
    temp_scripture["text_alterations"] = {
        "every_other":None,
        "first_three":None
    }

    # if temp_scripture["marked_text"] != scriptures[text], add '...' in appropriate places

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
