# YouTube Jukebox
Collaborative playlist creation with python, vlc, and a dash of bash

## Table of Contents
1. Dependencies
2. Setup
3. Use
4. Notes

## Dependencies
There aren't many dependencies for this program, though there are a few
1. This project uses Python 2.7 (You're more than welcome to try it on other versions, I just won't help you if something goes wrong!)
2. You'll need `flask`, `pafy`, and `youtube-dl`
    * I'm going to recommend using a python virtual environment
        * `pip install virtualenv`
        * `virtualenv -p /usr/bin/python2.7 ./venv`
        * `source ./venv/bin/activate`
        * You can exit the virtual environment with `deactivate`
    * You can install them with `pip install flash pafy youtube-dl`
3. You'll need VLC
    * You can install it with `sudo apt-get install vlc` (assuming you're debian based, otherwise just install vlc)

## Setup
Setup is really simple once you have all the dependencies in order, 
1. Open up a terminal and type
    * `python __main__.py`
2. Open VLC and set it up to run on only one instance
    * Tools -> Preferences
    * Click on "Interface"
    * Click "Allow only one instance"
    * Click on "Enqueue items into playlist in one instance mode"

And that's really it, the server is running! You should be able to get to it from `http://127.0.0.1:5000`, make some requests and then press play in VLC and the server will handle the rest!

## Notes
The only thing that I should really point out is that the server works by downloading the requests as an audio file from youtube then queueing them into VLC, therefore it will take up space on your machine while the server is running.
The queue is also generated via creating files on the machine, these also take up space (and will make things a little confusing between sessions).
You can take care of both of these by deleting the files in `notes` and `songs`, but please do not delete `addtovlc.sh` in the songs directory, that will break the auto queue feature.

## TODO
* Make it look somewhat decent
* Make scripts to clean out the temporary files (songs and queue, separately to allow a user to keep a playlist)
* Somehow fix unicode handling (it did NOT like when I tried to add an Alt-J song, due to the logo)