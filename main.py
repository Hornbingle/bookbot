from stats import word_count
from stats import letter_count

current_book = "books/frankenstein.txt"

def main():
    num_words = word_count(current_book)
    num_letters = letter_count(current_book)
    print(f"{num_words} words found in the document")
    print(num_letters)
    """print("============ BOOKBOT ============")
    print(f"Analyzing book found at {current_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")"""

main()