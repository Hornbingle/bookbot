current_book = "books/frankenstein.txt"

def get_book_test(current_book):
    with open(current_book) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(book_string):
    file_contents = get_book_test(book_string)
    split_contents = file_contents.split()
    words_number = 0
    for words in split_contents:
        words_number += 1
    return words_number

def letter_count(book_string):
    file_contents = get_book_test(book_string)
    lower_contents = file_contents.lower()
    letter_dictionary = {}
    for letter in lower_contents:
        variable_letter_count = 0
        vlc = variable_letter_count
        if letter in letter_dictionary:
            vlc = letter_dictionary[letter]
            vlc += 1
            letter_dictionary[letter] = vlc
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary