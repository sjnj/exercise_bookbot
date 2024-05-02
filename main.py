from collections import Counter
from string import ascii_lowercase
from typing import Dict

PATH_TO_BOOK = './books/frankenstein.txt' 

def total_words(text: str) -> int:
    """ Counts the number of words in 'text'. """
    return len(text.split())

def word_counter(text: str) -> Dict[str, int]:
    """Counts the frequency of each letter in the text. """
    text = text.lower()
    char_counter = Counter(text)
    letter_dict = {letter: freq for letter, freq in char_counter.most_common() if letter in ascii_lowercase}
    return letter_dict

def print_report(text: str) -> None:
    """Prints a report of the document word and letter counts. """
    print(f"--- Begin report of {PATH_TO_BOOK} ---")
    print(f"{total_words(text)} words found in the document")
    print("")
    for letter, freq in word_counter(text).items():
        print(f"The {letter} character was found {freq} times")
    print("--- End report ---")


def main():
    with open(PATH_TO_BOOK, 'r') as file:
        text_ = file.read()
    print_report(text_)

if __name__ == '__main__':
    main()
