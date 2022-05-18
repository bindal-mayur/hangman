class GameStateCodes:
    GAME_END = 0
    GAME_START = 1
    GAME_WON = 2
    GUESSED_ALREADY = 3
    OUT_OF_TRIES = 4
    LETTER_NOT_FOUND = 5
    LETTER_FOUND = 6
    SHOW_WORD_PROGRESS = 7
    GUESS_LETTER = 8

    status_messages = {
        GAME_START: "Do you wish to play Hangman ? [y/n]:",
        GAME_WON: "You won the game!",
        GUESSED_ALREADY: "You have guessed that letter before!",
        OUT_OF_TRIES: "You ran out of tries - you lose!",
        LETTER_NOT_FOUND: "This letter wasn't in the word - try again!",
        LETTER_FOUND: "You found a letter!",
        SHOW_WORD_PROGRESS: "Word guessed: ",
        GUESS_LETTER: "Please guess a letter: ",
        GAME_END: "Terminating game. Goodbye!"
    }
