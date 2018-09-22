#!/bin/bash

# Do this after testing the program

rm -f $HOME/binaries/ImageViewer/lin32.tar.bz2
tar -cvjSf $HOME/binaries/ImageViewer/lin32.tar.bz2 ./ImageViewer
rm -r ./ImageViewer
./clean_up.sh
