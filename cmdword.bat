@echo off

cd %USERPROFILE%\Desktop
echo hello desktop > desktop.txt

cd %USERPROFILE%\Downloads
echo hello download > download.txt

move "%USERPROFILE%\Downloads\download.txt" "%USERPROFILE%\Desktop"
move "%USERPROFILE%\Desktop\desktop.txt" "%USERPROFILE%\Downloads"

cd %USERPROFILE%\Desktop
echo hello im valley > valleyfile.txt

netstat -an -o > valleyfile.txt

find ":80" valleyfile.txt

del valleyfile.txt

pause
