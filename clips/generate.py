#!/bin/python

import argparse
import random
import subprocess

extension = ".mp3"
clips = [
    "Still-Alive-01",
    "Still-Alive-02",
    "Still-Alive-03",
    "Still-Alive-04",
    "Still-Alive-05",
    "Still-Alive-06",
    "Still-Alive-07",
    "Still-Alive-08",
    "Still-Alive-09",
    "Still-Alive-10",
    "Still-Alive-11",
    "Still-Alive-12",
    "Still-Alive-13",
    "Still-Alive-14",
    "Still-Alive-15",
    "Still-Alive-16",
    "Still-Alive-17",
    "Still-Alive-18",
    "Still-Alive-19",
    "Still-Alive-20",
    "Still-Alive-21",
    "Still-Alive-22",
    "Still-Alive-23",
    "Still-Alive-24",
    "Still-Alive-25",
    "Still-Alive-26",
    "Still-Alive-27",
    "Still-Alive-28",
    "Still-Alive-29",
    "Still-Alive-30",
    "Still-Alive-31",
    "Still-Alive-32",
    "Still-Alive-33",
    "Still-Alive-34",
    "Still-Alive-35",
    "Still-Alive-36",
    "Still-Alive-37",
    "Still-Alive-38"
]

clipsGrouped = [
    [   # 0 intro
        "Still-Alive-01",
        "Still-Alive-02",
        "Still-Alive-03",
        "Still-Alive-04",
        "Still-Alive-05",  # intro (with extra beat)
        "Still-Alive-06"
    ],
    [   # 1 intro (tempo change)
        "Still-Alive-07",
        "Still-Alive-08",
        "Still-Alive-09",
        "Still-Alive-10"
    ],
    [   # 2
        "Still-Alive-11",
        "Still-Alive-12",
        "Still-Alive-13",
        "Still-Alive-14",
        "Still-Alive-15",
        "Still-Alive-16"
    ],
    [   # 3
        "Still-Alive-17",
        "Still-Alive-18",
        "Still-Alive-19",
        "Still-Alive-20",
        "Still-Alive-21",
    ],
    [   # 4
        "Still-Alive-22",
        "Still-Alive-23",
        "Still-Alive-24",
    ],
    [   # 5
        "Still-Alive-25",
        "Still-Alive-26",
        "Still-Alive-27"
    ],
    [   # 6
        "Still-Alive-28",
        "Still-Alive-29",
        "Still-Alive-30",
        "Still-Alive-31",
        "Still-Alive-32",
        "Still-Alive-33",
        "Still-Alive-34",
        "Still-Alive-35",
        "Still-Alive-36",
        "Still-Alive-37",
        "Still-Alive-38"
    ]
]
groupTransitions = {
    0: [1, 4],
    1: [2, 5],
    2: [3, 5, 6],
    3: [4, 0],
    4: [5, 3],
    5: [6, 2, 3],
    6: [0]
}


def nextClip(groupId, clipId, randomize):
    # Determines the next clip to add to the filelist
    newGroupId = groupId
    newClipId = clipId

    # Full random so get any random clip
    if randomize:
        while newClipId == clipId:
            newClipId = random.randrange(0, len(clips))
    else:
        groupChanged = False

        # After playing the last clip in a group, transition to another group
        if clipId == len(clipsGrouped[groupId]) - 1:
            groupChanged = True
            while newGroupId == groupId:
                newGroupId = random.choice(groupTransitions[groupId])

        # Pick a clip from the current group
        while newClipId == clipId:
            newClipId = random.randrange(0, len(clipsGrouped[newGroupId]))

    return (newGroupId, newClipId)


def generate_file(iterations, randomize, ender):
    # generates a filelist of clips for ffmpeg to consume
    # iterations: how many clips to include
    # randomize: True if we try to group clips with a similar tempo
    # ender: True if we end the song with the normal song ender

    with open('filelist-generated', 'w', encoding='utf-8') as f:
        groupId = 0
        clipId = 0
        for i in range(0, iterations):
            groupId, clipId = nextClip(groupId, clipId, randomize)

            # Get the next clip name then write it to our filelist
            if i == iterations - 1 and ender:
                # Make sure the last clip is the proper ending if they want it
                clipName = clips[len(clips) - 1]
            elif randomize:
                clipName = clips[clipId]
            else:
                clipName = clipsGrouped[groupId][clipId]

            f.write('file {0}{1}\n'.format(clipName, extension))


def call_ffmpeg():
    # Calls ffmpeg to generate the final audio file
    subprocess.call(['ffmpeg',
                     '-f', 'concat',
                     '-safe', '0',
                     '-i', 'filelist-generated',
                     '-c', 'copy',
                     '-y',
                     'Still-Alive-Generated' + extension
                     ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates a random version '
                                                 'of Still Alive using ffmpeg.'
                                                 ' The generated song will be '
                                                 'called '
                                                 'Still-Alive-Generated{0}. It'
                                                 ' will also store the list of'
                                                 ' clips to be used in a file '
                                                 'called filelist-generated.'
                                                 .format(extension))
    parser.add_argument('iterations',
                        metavar='ITERATIONS',
                        type=int,
                        help='minimum number of clips to add')
    parser.add_argument('-r',
                        '--random',
                        help='Makes the clip selection completely random '
                             'instead of organized by tempo',
                        action='store_true')
    parser.add_argument('-n',
                        '--normalEnd',
                        help='Makes the last clip the normal song end clip '
                             'instead of a random one',
                        action='store_true')

    args = parser.parse_args()
    generate_file(args.iterations, args.random, args.normalEnd)
    call_ffmpeg()
