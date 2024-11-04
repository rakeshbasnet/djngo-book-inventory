import re


def validate_isbn(value):
    # Regex for ISBN-10 and ISBN-13, allowing hyphens
    isbn10_regex = r'^(ISBN(?:-10)?:? )?(?:[0-9]{9}[0-9X]|[0-9]{1,5}-[0-9]+-[0-9]+-[0-9]+-[0-9X])$'
    isbn13_regex = r'^(ISBN(?:-13)?:? )?(978|979)[- ]?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9]$'

    # Normalize value by removing hyphens for length and checksum validation
    normalized_value = re.sub(r'[-\s]', '', value)

    # Check if it matches ISBN-10
    if re.match(isbn10_regex, value):
        if not is_valid_isbn10(normalized_value):
            raise ValueError(f"Invalid ISBN-10 number: {value}")
    # Check if it matches ISBN-13
    elif re.match(isbn13_regex, value):
        if not is_valid_isbn13(normalized_value):
            raise ValueError(f"Invalid ISBN-13 number: {value}")
    else:
        raise ValueError(f"Invalid ISBN format: {value}")


def is_valid_isbn10(isbn):
    if len(isbn) != 10:
        return False
    total = sum(int(isbn[i]) * (10 - i) for i in range(9))
    checksum = (11 - (total % 11)) % 11
    if checksum == 10:
        checksum = 'X'
    return str(checksum) == isbn[-1]


def is_valid_isbn13(isbn):
    if len(isbn) != 13:
        return False
    total = sum(int(isbn[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
    checksum = (10 - (total % 10)) % 10
    return str(checksum) == isbn[-1]
