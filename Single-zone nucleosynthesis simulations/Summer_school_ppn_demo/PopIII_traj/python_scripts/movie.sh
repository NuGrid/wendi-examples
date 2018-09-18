#!/bin/bash
# assumes you have a series of png images, like Prefix000.png
# make a movie out of these with some reasonable defaults
# one arguments: Prefix
# example: movie.sh AbuChart
# if you want to change the size add -s 800x600
#ffmpeg  -y -f image2 -r 12 -pattern_type glob -i "$1*.png" -preset slow -crf 18 -s 800x600 out1.mp4
ffmpeg  -y -f image2 -r 12 -pattern_type glob -i "$1*.png" -preset slow -crf 18  $1.mp4
