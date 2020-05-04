def convert_u16(data: int) -> str:
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
