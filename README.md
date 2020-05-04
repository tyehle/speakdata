# speakdata
A very useful guide on how to pronounce byte sequences

```pycon
>>> import random
>>> import speakdata
>>> 
>>> data = [random.randint(0, 255) for _ in range(8)]
>>> 
>>> print(":".join(f"{byte:02x}" for byte in data))
ed:6f:16:9b:eb:a8:d0:07
>>> 
>>> print(speakdata.pronounce(data))
Toijeyting bownining tutul saibaking.
```
