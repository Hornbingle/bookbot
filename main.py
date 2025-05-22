from stats import word_count
from stats import letter_count
from stats import neat_output
import sys

number_of_sys_arguments = len(sys.argv)

def arguments_check():
    if number_of_sys_arguments < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        pass

arguments_check()

current_book = sys.argv[1]

def main():
    try:
        num_words = word_count(current_book)
        num_letters = letter_count(current_book)
        neat_counts = neat_output(current_book)
        """print(f"{num_words} words found in the document")
        print(num_letters)"""
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {current_book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        print(neat_counts)
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

"""def input_check():
    try:
        main()
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)"""

main()