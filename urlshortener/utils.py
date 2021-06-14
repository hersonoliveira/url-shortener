import string
import random


def _convert_to_base_62(id: int) -> list:
    """
    Convert an Integer to base 62 and return it's digits
    """
    digits = []
    dividend = id
    remainder = 0

    while dividend > 0:
        remainder = dividend % 62
        dividend //= 62
        digits.append(remainder)

    return digits


def _convert_digits_to_char(digits: list) -> list:
    """
    Convert digits to characters
    """
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    return [chars[digit] for digit in digits]


def generate_short_url(id: int, length: int = 7, base: str = "tier.app") -> str:
    """
    Generate short url from an int id
    """
    digits = _convert_to_base_62(id)

    if len(digits) < length:
        for _ in range(length - len(digits)):
            random_num = random.randint(0, 61)
            digits.append(random_num)
    
    hash = "".join(_convert_digits_to_char(digits))
    
    return f"{base}/{hash}"
