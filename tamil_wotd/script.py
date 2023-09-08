from words.models import Words

if Words:
    new = Words()
    new.meaning = "meaning"
    new.transliteration = "roman"
    new.example = "example sentence"
    new.save()

    print("Created new object!")
    print("Change the object fields by visiting /admin")
else:
    print("Error! No model found.")