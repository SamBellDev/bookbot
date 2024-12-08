from typing import Dict

def main():
    book_path: str = "books/frankenstein.txt"
    text: str = get_book_text(book_path)
    num_words: str = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_char_count(text: str) -> Dict[str, int]:
    # initialise a dict to store char counts
    # loop over each char in the text
    # convert text to lowercase
    # update dict entries as appropriate
    pass

def get_num_words(text: str) -> int:
    words: List[str] = text.split()
    return len(words)


def get_book_text(path: str) -> str:
    try:
        with open(path) as file:
            return file.read()
    except OSError as e:
        print(f"An error was raised when looking for the specified book: {e}")
        return "An error has occured. Failed to get book."

main()
