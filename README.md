# forever-still-alive

The song Still Alive from Portal has sets of lyrics that are mostly standalone. With that that, I created this in order to randomly select the lyrics and make an infinite length song.

There are a couple options. It can choose the lyrics (clips) completely randomly which can have a bit more jarring of a transition or it can try to keep similar tempos together to make it smoother.

There is a web version and a python/ffmpeg version that can be done locally. The web version can be viewed at https://bobjrsenior.com/etc/still-alive-forever.

Even though the song is [free on Steam](https://store.steampowered.com/app/323170/Portal_Soundtrack/), I want to avoid copyright issues and didn't include the lyric clips here. It is straightforward to generate them though.

## Requirements

In order to generate clips or use local generation, ffmpeg will need to be installed. To generate songs locally, you will also need python.

## Usage

### Generating clips

1. Download the Portal soundtrack for free here: https://store.steampowered.com/app/323170/Portal_Soundtrack/
2. Copy "12 Still Alive.mp3" (or Portal-12-Still_Alive.flac) into the clips folder of this repo
3. Rename the "12 Still Alive.mp3" (or Portal-12-Still_Alive.flac) track to Still-Alive.mp3 (or Still-Alive.flac)
4. If you want a flac version instead of mp3, open extract.sh and change the extension variable on line 3 to "flac"
5. Run the extract.sh script from the clips folder (it takes no arguments). Windows users can open the file to see the commands. It's not a complicated script.

## Web Version

After the clips are generated, the web version is just the .html file in the root of the repository and the generated clips. If you want it to use flac files, find the extension variable and change it to ".flac".

It can be run locally by just opening the html file in your browser or with your facorite web server.

Note: There tends to be a slight delay between clips playing in the web version

## Local Song Generation

After the clips are generated, the generate.py script in the clips folder can be used to generate songs.

The generated song will be called Still-Alive-Generated.mp3 (or Still-Alive-Generated.flac). It will also create a file called filelist-generated with the list of chosen clips.

If you want a flac version instead of mp3, open generate.py and change the extension variable on line 7 to ".flac".

Usage:

```
usage: generate.py [-h] [-r] [-n] ITERATIONS

Generates a random version of Still Alive using ffmpeg. The generated song
will be called Still-Alive-Generated.mp3. It will also store the list of clips
to be used in a file called filelist-generated.

positional arguments:
  ITERATIONS       minimum number of clips to add

options:
  -h, --help       show this help message and exit
  -r, --random     Makes the clip selection completely random instead of
                     organized by tempo
  -n, --normalEnd  Makes the last clip the normal song end clip instead of a
                   random one
```

Example 1: View the help message
```
./generate -h
```

Example 2: Generate a song with 10 grouping together clips with a similar tempo
```
./generate.py 10
```

Example 3: Generate a song with 8 completely random lyrics clips
```
./generate.py -r 8
```

Example 4: Generate a song with 15 completely random lyrics clips but end it with the normal song ending clip
```
./generate.py -r -n 15
```
