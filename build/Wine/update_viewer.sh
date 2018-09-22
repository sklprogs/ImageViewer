#!/bin/bash

./update_here.sh
./build.sh
mkdir -p ./ImageViewer/app
mv ./build/exe.win32-3.4/* ./ImageViewer/app/
rmdir -p build/exe.win32-3.4
cp -r $HOME/bin/shared_bin_win/* ./ImageViewer/app/
cp -r ./resources ./ImageViewer/
cp ./ImageViewer.cmd ./ImageViewer/

cd ImageViewer/app && wine ImageViewer.exe
read -p "Update the archive? (y/n) " choice
if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
	rm -f $HOME/binaries/ImageViewer/win32.zip
	cd ../.. && zip -rv $HOME/binaries/ImageViewer/win32.zip ImageViewer/ && rm -r ImageViewer
	./clean_up.sh
fi
