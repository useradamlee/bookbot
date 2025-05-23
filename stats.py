def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def num_character(filepath):
    character_count = {}
    text = get_book_text(filepath)
    formatted_text = text.lower()
    for character in formatted_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    sorted_dictionaries = []
    for character in dictionary:
        each_dictionary = {}
        each_dictionary["char"] = character
        each_dictionary["num"] = dictionary[character]
        sorted_dictionaries.append(each_dictionary)

    sorted_dictionaries.sort(reverse=True, key=sort_on)
    return sorted_dictionaries



def num_of_words(filepath):
    text = get_book_text(filepath)
    split_text = text.split()
    counter = 0
    for texts in split_text:
        counter += 1
    return counter

