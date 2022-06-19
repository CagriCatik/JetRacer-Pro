#!/bin/bash

set -eu -o pipefail # fail on error and report it, debug all lines

sudo -n true
test $? -eq 0 || exit 1 "(tput setaf 1)you should have sudo privilege to run this script $(tput sgr 0)"


echo "$(tput setaf 1)** Installing the must-have pre-requisites ** $(tput sgr 0)"
while read -r p ; do sudo apt-get install -y $p ; done < <(cat << "EOF"
    libsdl1.2-dev 
    python-dev 
    libsdl-image1.2-dev 
    libsdl-mixer1.2-dev 
    libsdl-ttf2.0-dev 
    libsdl1.2-dev 
    libsmpeg-dev 
    python-numpy 
    subversion 
    libportmidi-dev 
    ffmpeg 
    libswscale-dev 
    libavformat-dev 
    libavcodec-dev 
    libfreetype6-dev
    python3-pip 
    python3-yaml
    terminator
EOF
)

