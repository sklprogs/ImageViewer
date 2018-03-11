#!/bin/sh

# Do not use "verbose" in order to spot errors easily

# Remove shared resources
rm -f ./resources/{error.gif,info.gif,question.gif,warning.gif}

# Remove other ImageViewer resources
rm -f ./resources/locale/ru/LC_MESSAGES/ImageViewer.mo

# Remove ImageViewer image files
rm -f ./resources/Gnu_\(PSF\).png

# Remove ImageViewer Python files
rm -f ./ImageViewer.py

# Remove shared Python files
rm -f ./{gettext_windows.py,shared.py,sharedGUI.py}

# (Wine-only) Remove build scripts
rm -f ./{build.sh,clean_up.sh,ImageViewer.cmd,setup.py}

rmdir -p resources/locale/ru/LC_MESSAGES

ls .
