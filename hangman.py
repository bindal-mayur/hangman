import random
from collections import defaultdict

from utils.game_state_codes import GameStateCodes
from utils.input_validation_codes import InputValidationCodes
from utils.random_word import get_random_word


class Hangman:
    """The Hangman class stores hangman game specific information.

        Attributes:
            NUM_TRIES (int): Total number of allowed user guesses
            comp_gen_word (str): Computer generated word to be guessed
            guessed_letters (set): Set of unique letters already been tried
            num_tries (int): Currently available number of guesses
            guessed_word (list): List of letters guessed by user
            letter_indices (dict): Position of each letter in the computer
                                   word
    """
    NUM_TRIES = 7

    def __init__(self, word='', num_tries=NUM_TRIES):
        self.comp_gen_word = word
        self.game_state = GameStateCodes.GAME_END
        self.guessed_letters = set()
        self.num_tries = num_tries
        self.guessed_word = ['_'] * len(word)
        self.letter_indices = defaultdict(list)
        # Create dictionary to store list of index/indices of each character
        # in the computer generated word to speed up the search process
        # when the user guesses a letter
        for pos, item in enumerate(word):
            self.letter_indices[item].append(pos)

    @staticmethod
    def play_hangman():
        """
        play_hangman function gives user a choice to play
        or end the game

        :returns: User's choice as a boolean value
        :rtype: bool
        """
        while True:
            user_input = input(
                    GameStateCodes.status_messages[
                        GameStateCodes.GAME_START]).lower()
            if user_input not in InputValidationCodes.valid_values[
                    InputValidationCodes.NOT_YES_NO]:
                print(InputValidationCodes.error_messsages[
                    InputValidationCodes.NOT_YES_NO])
            elif user_input == InputValidationCodes.YES:
                return True
            else:
                return False

    def guess_letter(self):
        """
        guess_letter function loops until user inputs a valid alphabet
        that hasn't been guessed before

        :returns: Alphabet entered by the user
        :rtype: str
        """
        self.game_state = GameStateCodes.GUESS_LETTER
        while True:
            user_input = input(
                    GameStateCodes.status_messages[
                        self.game_state]).lower()
            if user_input not in InputValidationCodes.valid_values[
                    InputValidationCodes.LETTER_NOT_ALPHA]:
                print(InputValidationCodes.error_messsages[
                    InputValidationCodes.LETTER_NOT_ALPHA])
            else:
                return user_input

    def show_grid(self):
        """
        show_grid function displays the alphabets in their correct
        position in the computer generated word to be guessed that
        have been guessed by the user so far the word. Letters not
        guessed yet will be displayed as '_'.
        """
        self.game_state = GameStateCodes.SHOW_WORD_PROGRESS
        print(f"{GameStateCodes.status_messages[self.game_state]}"
              f"{' '.join(self.guessed_word)}")

    def search_letter(self, letter):
        """
        search_letter function is used to search the user entered
        letter in the computer generated word and update the state
        of the game accordingly

        :param letter: User guessed alphabet
        :type letter: str
        """
        if letter in self.guessed_letters:
            self.game_state = GameStateCodes.GUESSED_ALREADY
            return
        self.guessed_letters.add(letter)
        if letter not in self.comp_gen_word:
            self.num_tries -= 1
            if self.num_tries == 0:
                self.game_state = GameStateCodes.OUT_OF_TRIES
                return
            self.game_state = GameStateCodes.LETTER_NOT_FOUND
        else:
            for index in self.letter_indices[letter]:
                self.guessed_word[index] = letter
            if '_' not in self.guessed_word:  # All letters have been guessed
                self.game_state = GameStateCodes.GAME_WON
                return
            self.game_state = GameStateCodes.LETTER_FOUND


if __name__ == '__main__':
    while Hangman.play_hangman():
        comp_generated_word = get_random_word()
        hangman = Hangman(word=comp_generated_word)
        while hangman.num_tries:
            print(f'{hangman.num_tries} attempts remain.')
            hangman.show_grid()
            letter_guessed = hangman.guess_letter()
            hangman.search_letter(letter_guessed)
            print(GameStateCodes.status_messages[hangman.game_state])
            if hangman.game_state == GameStateCodes.GAME_WON:
                break
        print(f'The correct word is {hangman.comp_gen_word}')
    print(GameStateCodes.status_messages[GameStateCodes.GAME_END])
