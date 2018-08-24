#!/bin/sh

# Do this after testing the program

rm -f $HOME/binaries/ImageViewer/linux.tar.bz2
tar -cvjSf $HOME/binaries/ImageViewer/linux.tar.bz2 ./ImageViewer
rm -r ./ImageViewer
./clean_up.sh
