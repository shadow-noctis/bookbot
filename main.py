def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    print(f"wordcount of document:{num_words}")
    #print(text)

def wordcount(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main ()

