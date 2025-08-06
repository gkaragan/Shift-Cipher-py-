import string
from random import choice
import sys
from ast import literal_eval


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("-e", "-d"):
        sys.exit("Usage: shift_cypher.py -e|-d")
    elif sys.argv[1] == "-e":
        message = input("Enter the message you wish to encrypt: \n")
        print(encrypt(message))
    else:
        message = literal_eval(
            input(
                "Enter the message (surrounded by quotation marks) and the shift values you have received as a tuple (e.g., ('abc', 12, 2)): \n"
            )
        )
        print(decrypt(*message))


def encrypt(message: str):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    letter_shift = choice(range(1, 26))
    digit_shift = choice(range(1, 10))

    # These are the versions of the strings after this shift value (translation) is applied
    # Note that the shift is in the counterclockwise direction
    shifted_lower = lower[letter_shift:] + lower[:letter_shift]
    shifted_upper = upper[letter_shift:] + upper[:letter_shift]
    shifted_digits = digits[digit_shift:] + digits[:digit_shift]

    chars = lower + upper + digits
    shifted_chars = shifted_lower + shifted_upper + shifted_digits

    # Translation table for the subsequent line to apply the shift in one pass over the string
    table = str.maketrans(chars, shifted_chars)

    return message.translate(table), letter_shift, digit_shift
    # A tuple of the form ('abc', 13, 5) is returned.
    # The 2 keys (letter_shift, digit_shift) are required to decrypt the encrypted message.
    # In practice, when sending the encrypted message these should be kept private between the two communicating.


def decrypt(message: str, letter_shift: int, digit_shift: int):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    shifted_lower = lower[letter_shift:] + lower[:letter_shift]
    shifted_upper = upper[letter_shift:] + upper[:letter_shift]
    shifted_digits = digits[digit_shift:] + digits[:digit_shift]

    chars = lower + upper + digits
    shifted_chars = shifted_lower + shifted_upper + shifted_digits
    table = str.maketrans(shifted_chars, chars)

    return message.translate(table)


if __name__ == "__main__":
    main()

