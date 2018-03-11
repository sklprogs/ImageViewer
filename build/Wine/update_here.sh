#!/bin/sh

# Do not use "verbose" in order to spot errors easily

mkdir -p ./resources/locale/ru/LC_MESSAGES/

# Copy shared resources
cp -u /usr/local/bin/shared/resources/{error.gif,info.gif,question.gif,warning.gif} ./resources/

# Copy ImageViewer image files
cp -u /usr/local/bin/ImageViewer/resources/Gnu_\(PSF\).png ./resources

# Copy other ImageViewer resources
cp -u /usr/local/bin/ImageViewer/resources/locale/ru/LC_MESSAGES/ImageViewer.mo ./resources/locale/ru/LC_MESSAGES/

# Copy ImageViewer Python files
cp -u /usr/local/bin/ImageViewer/src/ImageViewer.py .

# Copy shared Python files
cp -u /usr/local/bin/shared/src/{gettext_windows.py,shared.py,sharedGUI.py} .

# (Wine-only) Copy build scripts
cp -u /usr/local/bin/ImageViewer/build/Wine/{build.sh,clean_up.sh,ImageViewer.cmd,setup.py} .

ls .
