import string


class InputValidationCodes:
    LETTER_NOT_ALPHA = 1
    NOT_YES_NO = 2
    YES = 'y'
    NO = 'n'
    error_messsages = {
        LETTER_NOT_ALPHA: "Letter must be an alphabetic character",
        NOT_YES_NO: "Invalid choice. Please enter 'y' or 'n'"
    }
    valid_values = {
        NOT_YES_NO: (YES, NO),
        LETTER_NOT_ALPHA: tuple(string.ascii_lowercase)
    }
