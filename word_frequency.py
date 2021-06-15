import string

import random

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename='one-today.txt'):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string, lowercasing the  
        text and get all the words from the text.
        """
        with open(self.filename) as file:
            text = file.read().lower()
            return text


file = FileReader()
print(file.read_contents())


class WordList:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self, text):
        """
        This method
        is responsible for stripping
        words of punctuation.
        """
        new_text_string = ""
        punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        for word in self.text:
            if word not in punctuation:
                new_text_string += word
        return new_text_string
    
    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        # words_to_count = []
        # for word in file

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """

list_of_words = WordList()
print(list_of_words.remove_punctuation())
# # print(list_of_words.remove_stop_words())
# # print(list_of_words.get_freqs())

class FreqPrinter:
    def __init__(self, freqs):
        pass

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        raise NotImplementedError("FreqPrinter.print_freqs")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
