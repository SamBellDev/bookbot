from typing import Dict, List
import sys

def main():
    book_path: str = "books/frankenstein.txt"
    try:
        text: str = get_book_text(book_path)
        num_words: int = get_num_words(text)
        char_counts: Dict[str, int] = get_char_count(text)
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print("\nCharacter counts:")
        for character, count in sorted(char_counts.items()):
            if character.isalpha():
                print(f"The '{character}' character appears {count} times")
        print(f"--- End report ---")
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_char_count(text: str) -> Dict[str, int]:
    if not text:
        return {}

    char_counts: Dict[str, int] = {}
    normalised_text: str = text.lower()

    for character in normalised_text:
        char_counts[character] = char_counts.get(character, 0) + 1
    return char_counts 

def get_num_words(text: str) -> int:
    if not text:
        return 0
    words: List[str] = text.split()
    return len(words)


def get_book_text(path: str) -> str:
    try:
        with open(path) as file:
            return file.read()
    except OSError as e:
        raise RuntimeError(f"Failed to read book at {path}: {e}")

if __name__ == "__main__":
    main()
