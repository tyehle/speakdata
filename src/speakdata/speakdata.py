"""Pronounce binary data.

This module exports two useful functions, pronounce and denounce. They are used
to convert binary data into pronouncable words and back.
"""

import re


_VOWELS = ["a", "i", "u", "oi", "ai", "ow", "ey", "or"]  # 3 bits
_CONSONANTS = "bfjklnst"  # 3 bits


def convert_u16(data: int) -> str:
    """Convert a 16 bit unsigned number into a word."""
    if data < 0 or data >= 2 ** 16:
        raise ValueError(f"Not a u16: {data}")

    # get the 16th bit by maybe adding *ing
    #  c    v    c    v    c  ing?
    # ...  ...  ...  ...  ...  .
    # total 16 bits

    return (
        _CONSONANTS[data >> 13 & 7]
        + _VOWELS[data >> 10 & 7]
        + _CONSONANTS[data >> 7 & 7]
        + _VOWELS[data >> 4 & 7]
        + _CONSONANTS[data >> 1 & 7]
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
    if not data:
        return ""

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
        sentence.append(convert_u16(partial[0] << 8))
    if sentence:
        result.append(" ".join(sentence).capitalize())
    return ". ".join(result) + "."


def denounce(sentences: str) -> bytes:
    """Convert a pronounced string back into bytes.

    If the input was an odd number of bytes then this function will output a
    byte sequence with a trailing zero byte.

    Example:
        >>> speakdata.denounce('Jowseyting kowsubing.')
        b'Wow!'

    Args:
        sentences: A sentence produced by `speakdata.pronounce`

    Returns:
        A byte sequence with a possible extra zero byte at the end
    """
    if sentences == "":
        return b""

    output = []
    for word in re.split(r"\.? ", sentences[:-1]):
        # This is the worst parser ever
        word = word.lower()

        c0 = max((c for c in _CONSONANTS if word.startswith(c)), key=len)
        word = word[len(c0) :]

        v0 = max((v for v in _VOWELS if word.startswith(v)), key=len)
        word = word[len(v0) :]

        c1 = max((c for c in _CONSONANTS if word.startswith(c)), key=len)
        word = word[len(c1) :]

        v1 = max((v for v in _VOWELS if word.startswith(v)), key=len)
        word = word[len(v1) :]

        c2 = max((c for c in _CONSONANTS if word.startswith(c)), key=len)
        word = word[len(c2) :]

        ending = word

        number = (
            _CONSONANTS.index(c0) << 13
            | _VOWELS.index(v0) << 10
            | _CONSONANTS.index(c1) << 7
            | _VOWELS.index(v1) << 4
            | _CONSONANTS.index(c2) << 1
            | (1 if ending == "ing" else 0)
        )

        output.append(number >> 8)
        output.append(number & 0xFF)

    return bytes(output)
