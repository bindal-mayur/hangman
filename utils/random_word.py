import os
import random
import yaml


FILE_NAME = "eng_words.yaml"


def get_random_word(file_name=FILE_NAME):
    """
    This function will retun a random word from a file
    containing words from english dictionary
    param filepath: Path of file containing words
    type filepath: str
    returns: A word from english dictionary
    rtype: str
    """
    valid_word = False
    random_word = ''
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)
    with open(file_path, 'r') as f:
        eng_word_list = yaml.safe_load(f)
        while(not valid_word):
            index = random.randint(0, len(eng_word_list) - 1)
            random_word = eng_word_list[index].lower()
            if random_word.isalpha():
                valid_word = True
    return random_word
