# validators.py
from django.core.exceptions import ValidationError
import re


def validate_isbn(value):
    """
    Validates an ISBN value. Accepts ISBN-10 and ISBN-13 formats.
    Raises a ValidationError if the ISBN is invalid.

    :param value: str - The ISBN to validate.
    """
    # Regular expressions for ISBN-10 and ISBN-13 (both with optional hyphens).
    isbn10_regex = r'^(ISBN(?:-10)?:? )?(?:[0-9]{9}[0-9X]|[0-9]{1,5}-[0-9]+-[0-9]+-[0-9]+-[0-9X])$'
    isbn13_regex = r'^(ISBN(?:-13)?:? )?(978|979)[- ]?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9]$'

    # Normalize by removing hyphens and spaces to make checksum validation easier.
    normalized_value = re.sub(r'[-\s]', '', value)

    # Check if it's ISBN-10 and validate checksum.
    if re.match(isbn10_regex, value):
        if not is_valid_isbn10(normalized_value):
            raise ValidationError(f"Invalid ISBN-10 number: {value}")
    # Check if it's ISBN-13 and validate checksum.
    elif re.match(isbn13_regex, value):
        if not is_valid_isbn13(normalized_value):
            raise ValidationError(f"Invalid ISBN-13 number: {value}")
    # If it doesn't match either ISBN-10 or ISBN-13 pattern, raise an error.
    else:
        raise ValidationError(f"Invalid ISBN format: {value}")


def is_valid_isbn10(isbn):
    """
    Validates the checksum for ISBN-10.

    :param isbn: str - The normalized ISBN-10 number (without hyphens).
    :return: bool - True if valid, False otherwise.
    """
    if len(isbn) != 10:
        return False
    total = sum(int(isbn[i]) * (10 - i) for i in range(9))
    checksum = (11 - (total % 11)) % 11
    if checksum == 10:
        checksum = 'X'
    return str(checksum) == isbn[-1]


def is_valid_isbn13(isbn):
    """
    Validates the checksum for ISBN-13.

    :param isbn: str - The normalized ISBN-13 number (without hyphens).
    :return: bool - True if valid, False otherwise.
    """
    if len(isbn) != 13:
        return False
    total = sum(int(isbn[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
    checksum = (10 - (total % 10)) % 10
    return str(checksum) == isbn[-1]
