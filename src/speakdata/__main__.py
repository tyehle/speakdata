import sys

import speakdata


def console_entry() -> None:
    if len(sys.argv) >= 2:
        with open(sys.argv[1], "rb") as handle:
            data = handle.read()
    else:
        data = sys.stdin.buffer.read()
    print(speakdata.pronounce(data))


if __name__ == "__main__":
    console_entry()
