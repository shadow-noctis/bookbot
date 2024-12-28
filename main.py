def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    characters = characters_list(text)
    print("--Beginning report of frankenstein.txt--")
    print(f"{num_words} words found in the document")
    print(f"Characters calculated: {characters_list(text)}")
    print("--End of report--")



def characters_list(text):
    num_characters = {}
    lowercased_book = text.lower()
    for character in lowercased_book:
        if character not in num_characters:
            num_characters[character] = 1
        else:
            num_characters[character] +=1
    return num_characters




def wordcount(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main ()

