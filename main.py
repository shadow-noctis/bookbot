def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    characters = characters_list(text)
    dict_list = list_of_dicts(characters)
    sorted_dictionary = sort_dictionary(characters)
    print("--Beginning report of frankenstein.txt--")
    print(f"{num_words} words found in the document")
    print("")
    for key, value in sorted_dictionary.items():
        print(f"The '{key}' character was found '{value}' times")
    print("")
    print("--End of report--")




def characters_list(text):
#Character dictionary
    num_characters = {}
    lowercased_book = text.lower()
    for character in lowercased_book:
        if character not in num_characters:
            num_characters[character] = 1
        else:
            num_characters[character] +=1
    filtered_counts = {key: value for key, value in num_characters.items() if key.isalpha()}
    return filtered_counts


def sort_dictionary(dictionary):
    sorted_items = sorted(dictionary.items(), reverse=True, key=lambda item: item[1])
    sorted_dict = dict(sorted_items)
    return sorted_dict


def list_of_dicts(characters):
    characters_list = []
    for key in characters:
        value = characters[key]
        characters_list.append({characters[key], key})
    return characters_list


def wordcount(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main ()

