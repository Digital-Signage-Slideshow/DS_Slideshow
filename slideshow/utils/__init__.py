import secrets
import random
import string
from slugify import slugify


def slugify_text(text, length=50) -> str:
    """
    Slugify text and return a substring of length `length`.
    text: str
    length: int
    """
    return slugify(text, separator='_', max_length=length, word_boundary=True, save_order=True)


def generate_random_string(length=10) -> str:
    """
    Generate a random string of length `length`.
    length: int
    """
    i = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return slugify_text(i)


def get_file_extension(filename: str) -> str:
    """
    Get the extension of a file.
    filename: str
    """
    return filename.split('.')[-1]


def get_filename(filename: str) -> str:
    """
    Get the filename of a file.
    filename: str
    """
    return filename.split('.')[0]
