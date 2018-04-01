# stereo-to-left-mono

This Python script scans the directory for stereo audio files (currently only works for .m4a), then outputs files containing the extracted left channels. 

## Usage

Place the script in a folder together with the audio files then:

```
python stereo-to-left-mono.py
```

The left mono files will have `_L` appended to the filename.


## Requirements

For this script to work, you will need [Pydub](https://github.com/jiaaro/pydub). To install:

```
pip install pydub
```

Pydub in turn requires [ffmpeg](https://www.ffmpeg.org) (unless your audio is .wav, in which case Pydub can work using native python audio functions). Note that the Pydub documentation on obtaining ffmpeg didn't work for me, but what did work was:

```
apt-get install libav-tools libav-tools
```

## Motivation

With the decline of jazz and limited social connectability, increasingly for a jazz pianist, the closest one can get to jamming with fellow musicians is with backing tracks. [Jamey Aebersold](https://en.wikipedia.org/wiki/Jamey_Aebersold) has produced 100s of such [backing tracks](https://en.wikipedia.org/wiki/List_of_songs_in_Aebersold%27s_%22Play-A-Long%22_series) since 1967 with musicians such as Ron Carter, Kenny Barron and Joey de Francesco. Since he started recording these tracks, Jamey has always put drums + bass on the left channel, and piano + drums on the right channel. Presumably, at the time this was the best way to separately encode two different mixes on a single stereo channel. Back in the day, most hifi systems would have a 'L-R Balance' knob, so it was trivial to pan to either channel as required. (Alternatively you, could just disconnect one speaker.)

With today's technology, ironically the task of isolating one channel from a regular stereo track has become not so trivial. This python script has helped me batch-process the extraction of the bass-drum track (which is the track I am interested in, seeing that I am a pianist), so I can jam with the greats to my heart's content :)

## Improvements/Todo

- Make it work for the other formats supported by ffmpeg, e.g. mp3, ogg etc. etc. (I buy my Aebersold tracks from Apple iTunes, which is why it currently only works with .m4a)

- Enable it to extract the right channel instead (for all those bassplayers who want a piano-drums track to play along with)


