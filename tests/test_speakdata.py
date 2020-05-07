import speakdata

import random


def test_convert_u16() -> None:
    assert speakdata.convert_u16(0) == "babab"
    assert speakdata.convert_u16(1) == "bababing"
    assert speakdata.convert_u16(2 << 0) == "babaf"
    assert speakdata.convert_u16(2 << 3) == "babib"
    assert speakdata.convert_u16(2 << 6) == "bafab"
    assert speakdata.convert_u16(2 << 9) == "bibab"
    assert speakdata.convert_u16(2 << 12) == "fabab"


def test_pronounce() -> None:
    assert speakdata.pronounce(b"") == ""
    assert speakdata.pronounce(b"Yes!") == "Jeyjeyjing kaisubing."
    assert speakdata.pronounce(b"\xff\x00") == "Torsab."
    assert speakdata.pronounce(b"\xff") == "Torsab."


def test_denounce() -> None:
    assert speakdata.denounce("") == b""
    assert speakdata.denounce("Jeyjeyjing kaisubing.") == b"Yes!"
    assert speakdata.denounce("fabab.") == bytes([0x20, 0x00])


def test_round_trip_fuzz() -> None:
    for _ in range(1000):
        size = random.randint(0, 50)
        data = bytes(random.randint(0, 255) for _ in range(size))
        expected = data if size % 2 == 0 else data + b"\0"
        assert speakdata.denounce(speakdata.pronounce(data)) == expected
