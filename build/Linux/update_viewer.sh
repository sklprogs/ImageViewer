#!/bin/bash

# Do not use "verbose" in order to spot errors easily

./update_here.sh
./build.sh
mkdir -p ImageViewer/app
cp -r resources ./ImageViewer
mv build/exe.linux-i686-3.4/* ./ImageViewer/app
rmdir -p build/exe.linux-i686-3.4
rm -r ./ImageViewer/app/{libicudata.so.54,libicui18n.so.54,libicuuc.so.54,libQt*,platforms,imageformats}
rm -r ./ImageViewer/app/lib/python3.4/{pymorphy*,PyQt5}
ls --color=always .
