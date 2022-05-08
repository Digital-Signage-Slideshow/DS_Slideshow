from slugify import slugify


def slugify_text(text, length=50) -> str:
    """
    Slugify text and return a substring of length `length`.
    text: str
    length: int
    """
    return slugify(text, separator='_', max_length=length, word_boundary=True, save_order=True)
