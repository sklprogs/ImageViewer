#!/bin/bash

# Do not use "verbose" in order to spot errors easily

# Remove shared resources
rm -f ./resources/{error.gif,info.gif,question.gif,warning.gif}

# Remove other ImageViewer resources
rm -f ./resources/locale/ru/LC_MESSAGES/ImageViewer.mo
rm -f ./resources/icon_64x64_viewer.gif

# Remove ImageViewer image files
rm -f ./resources/Gnu_\(PSF\).png

# Remove ImageViewer Python files
rm -f ./ImageViewer.py

# Remove shared Python files
rm -f ./{gettext_windows.py,shared.py,sharedGUI.py}

# (Linux-only) Remove build scripts
rm -f ./{build.sh,clean_up.sh,setup.py,update_finish.sh,update_here.sh,update_viewer.sh}

rmdir -p resources/locale/ru/LC_MESSAGES

ls .
