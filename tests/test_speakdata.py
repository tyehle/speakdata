import speakdata


def test_convert_u16() -> None:
    assert speakdata.convert_u16(0) == "babab"
    assert speakdata.convert_u16(1) == "bababing"
    assert speakdata.convert_u16(2 << 0) == "babaf"
    assert speakdata.convert_u16(2 << 3) == "babib"
    assert speakdata.convert_u16(2 << 6) == "bafab"
    assert speakdata.convert_u16(2 << 9) == "bibab"
    assert speakdata.convert_u16(2 << 12) == "fabab"


def test_pronounce() -> None:
    assert speakdata.pronounce(b"Yes!") == "Jeyjeyjing kaisubing."
