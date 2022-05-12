#!/bin/bash

extension=mp3
ffmpeg -f concat -safe 0 -i filelist-ordered -c copy concatenated.$extension
