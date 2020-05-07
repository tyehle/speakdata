# speakdata
![Build](https://github.com/tyehle/speakdata/workflows/Build/badge.svg)

A very useful guide on how to pronounce byte sequences.

Have you ever looked for a quick and easy way to say `84:a3:fe:67:c5:01`, or maybe `192.168.0.1`?

Look no further! `speakdata` is a canonical way to translate bytes into easy pronouncable syllables. For more info have a look at [this post](https://tobin.yehle.us/articles/speakdata).

```pycon
>>> import speakdata
>>>
>>> speakdata.pronounce([192, 168, 0, 1])
'Saful bababing.'
>>>
>>> speakdata.pronounce(b'\x84\xa3\xfe\x97\xc5\x01')
'Lifufing torniking sijabing.'
>>> 
>>> speakdata.denounce('Lifufing torniking sijabing.')
b'\x84\xa3\xfe\x97\xc5\x01'
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
