# speakdata
A very useful guide on how to pronounce byte sequences.

Have you ever looked for a quick and easy way to say `84:a3:fe:67:c5:01`, or maybe `192.168.0.1`?

Look no further! `speakdata` is a canonical way to translate bytes into easy pronouncable syllables. For more info have a look at [this post](https://tobin.yehle.us/articles/speakdata).

```pycon
>>> import speakdata
>>>
>>> speakdata.pronounce(b'\x84\xa3\xfe\x67\xc5\x01')
'Lifufing torleyking sijabing.'
>>>
>>> speakdata.pronounce([192, 168, 0, 1])
'Saful bababing.'
```

It also has a nifty executable:

```shell
$ head -c 24 /dev/random | speakdata
Lafoin fowkoising joiboiling tubaiking jujowl fowsain sowtat jiforn. Naijoiking seynij nujoiting korsul.
```

# Installation

```shell
pip install speakdata
```
