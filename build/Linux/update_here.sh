#!/bin/bash

# Do not use "verbose" in order to spot errors easily

mkdir -p ./resources/locale/ru/LC_MESSAGES/

# Copy shared resources
cp -u $HOME/bin/shared/resources/{error.gif,info.gif,question.gif,warning.gif} ./resources/

# Copy ImageViewer image files
cp -u $HOME/bin/ImageViewer/resources/Gnu_\(PSF\).png ./resources/

# Copy other ImageViewer resources
cp -u $HOME/bin/ImageViewer/resources/locale/ru/LC_MESSAGES/ImageViewer.mo ./resources/locale/ru/LC_MESSAGES/
cp -u $HOME/bin/ImageViewer/resources/icon_64x64_viewer.gif ./resources/

# Copy ImageViewer Python files
cp -u $HOME/bin/ImageViewer/src/ImageViewer.py .

# Copy shared Python files
cp -u $HOME/bin/shared/src/{gettext_windows.py,shared.py,sharedGUI.py} .

# (Linux-only) Copy build scripts
cp -u $HOME/bin/ImageViewer/build/Linux/{build.sh,clean_up.sh,setup.py,update_finish.sh,update_viewer.sh} .

ls --color=always .
