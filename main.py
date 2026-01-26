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

    # Load the Landmark Verses
    landmark_verses = load_scriptures('bridgers-landmarks.txt')
    print("here")
    
    # ****Just for demonstrations purposes only****
    scripture = {
        "source_book":"Book of Mormon",
        "book":"1 Nephi",
        "chapter":1,
        "verse":1,
        "text":"I, Nephi, having been born of goodly parents, therefore I was taught somewhat in all the learning of my father; and having seen many afflictions in the course of my days, nevertheless, having been highly favored of the Lord in all my days; yea, having had a great knowledge of the goodness and the mysteries of God, therefore I make a record of my proceedings in my days.",
# Instead of saving different alterations, have the way it is displayed change dynamically according to the following options:
# 1) Percentage Slider: takes out words by percentage at equal intervals, for example 50% would be every other word.
# 2) Word Size: takes out all words of a certain size, for example you could take out all words 4 letters or shorter, or 7 letters or greater, etc.
# 3) Line Mastery: only displays the first 3 words of each line
# 4) Customization: you select which words or sections to remove and save it as an option
#       - you can create as many customizations per verse as you'd like.
        "text_alterations":{
            "every_other":None,
            "first_three":None
        }
    }

    # Take the text and save some different options
    words = scripture["text"].split()
    
    # Every other word replaced with '___'
    every_other_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            every_other_words.append(word)
        else:
            every_other_words.append("___")
    scripture["text_alterations"]["every_other"] = " ".join(every_other_words)

    # First 3 words only
    scripture["text_alterations"]["first_three"] = " ".join(words[:3])

    print(
        f"FULL SCRIPTURE"
        f"Source: {scripture['source_book']}\n"
        f"Reference: {scripture['book']} {scripture['chapter']}:{scripture['verse']}\n"
        f"{scripture['text']}"
    )

    print(
        f"SCRIPTURE 50%\n"
        f"Reference: {scripture['book']} {scripture['chapter']}:{scripture['verse']}\n"
        f"{scripture['text_alterations']['every_other']}\n"
    )

    print(
        f"REFERENCE AND 3\n"
        f"Reference: {scripture['book']} {scripture['chapter']}:{scripture['verse']}\n"
        f"{scripture['text_alterations']['first_three']}\n"
    )

    

if __name__ == "__main__":
    main()