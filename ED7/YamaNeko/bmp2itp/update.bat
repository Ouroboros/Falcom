@ECHO OFF

cd/d "%~dp0"

uci2itp.exe bface000.bmp
copy /y bface000.itp J:\Falcom\ED_Zero\patch\battle\itp\bface000.itp
J:\Falcom\ED_Zero\patch\battle\itp\YamaNeko.exe J:\Falcom\ED_Zero\patch\battle\itp\bface000.itp
