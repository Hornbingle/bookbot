current_book = "books/frankenstein.txt"

def get_book_test(current_book):
    with open(current_book) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(current_book):
    file_contents = get_book_test(current_book)
    split_contents = file_contents.split()
    words_number = 0
    for words in split_contents:
        words_number += 1
    return words_number

def letter_count(current_book):
    file_contents = get_book_test(current_book)
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

def sort_criteria(unsorted_dictionary_list):
    return unsorted_dictionary_list["count"]

def list_of_dictionaries(current_book):
    unsorted_dictionary = letter_count(current_book)
    unsorted_dictionary_list = []
    for key in unsorted_dictionary:
        temp_dictionary = {}
        temp_dictionary["character"] = key
        temp_dictionary["count"] = unsorted_dictionary[key]
        unsorted_dictionary_list.append(temp_dictionary)
    unsorted_dictionary_list.sort(reverse=True, key=sort_criteria)
    return unsorted_dictionary_list

def neat_output(current_book):
    sdl = list_of_dictionaries(current_book)
    output_string = ""
    for dictionaries in sdl:
        temp_string = ""
        temp_character = dictionaries["character"]
        temp_count = dictionaries["count"]
        temp_string = f"{temp_character}: {temp_count}\n"
        output_string += temp_string
    return output_string

#neat_output(current_book)