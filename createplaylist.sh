#!/bin/bash

(cd youtubejukebox/notes && ls -v | xargs cat) >> playlist.txt
