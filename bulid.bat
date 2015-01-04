@echo off
rmdir /s /q dist
call cxfreeze.bat pianoEmulator.py --target-dir dist --base-name=win32gui
copy keyboardMap.png dist
copy pianoBoard.bmp dist
copy ReadMe.html dist
copy ReadMe.markdown dist
xcopy music dist\music\