import speakdata


def test_convert_u16() -> None:
    assert speakdata.convert_u16(53914) == "sainin"
    assert speakdata.convert_u16(53915) == "sainining"


def test_pronounce() -> None:
    assert speakdata.pronounce(b"Yes!") == "Jeyjeyjing kaisubing."
