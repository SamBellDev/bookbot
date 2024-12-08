def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_char_count(text: string) -> dict:
    # initialise a list of unique alphabet characters

def get_num_words(text: string) -> int:
    words = text.split()
    return len(words)


def get_book_text(path: string) -> string:
    with open(path) as file:
        return file.read()


main()
