"""Pronounce binary data.

This module exports only one useful function, pronounce. It is used to convert
binary data into pronouncable words.
"""


def convert_u16(data: int) -> str:
    """Convert a 16 bit unsigned number into a word."""
    if data < 0 or data >= 2 ** 16:
        raise ValueError(f"Not a u16: {data}")

    vowels = ["a", "i", "u", "oi", "ai", "ow", "ey", "or"]  # 3 bits
    consonants = "bfjklnst"  # 3 bits

    # get the 16th bit by maybe adding *ing
    #  c    v    c    v    c  ing?
    # ...  ...  ...  ...  ...  .
    # total 16 bits

    return (
        consonants[data >> 13 & 7]
        + vowels[data >> 10 & 7]
        + consonants[data >> 7 & 7]
        + vowels[data >> 4 & 7]
        + consonants[data >> 1 & 7]
        + ("ing" if data & 1 == 1 else "")
    )


def pronounce(data: bytes) -> str:
    """Convert a byte sequence into a string.

    Every two bytes becomes a word, and every 8 words becomes a sentence. If
    there are an odd number of bytes then a zero byte fills out the last word.

    Example:
        >>> speakdata.pronounce([192, 168, 0, 1])
        'Saful bababing.'

    Args:
        data: A byte sequence to pronounce

    Returns:
        A pronouncable string representing the the given bytes
    """
    result = []
    sentence = []
    partial = []
    for byte in data:
        partial.append(byte)
        if len(partial) == 2:
            number = (partial[0] << 8) + partial[1]
            sentence.append(convert_u16(number))
            partial = []
            if len(sentence) == 8:
                result.append(" ".join(sentence).capitalize())
                sentence = []
    if partial:
        sentence.append(convert_u16(partial[0]))
    if sentence:
        result.append(" ".join(sentence).capitalize())
    return ". ".join(result) + "."
