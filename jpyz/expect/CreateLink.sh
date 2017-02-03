#!/bin/bash
# CreateLink.sh

filePath="$HOME/Desktop/"
fileName="openvpn.py"
linkFileName="$filePath$fileName"
targetPath="$(pwd)/"
targetFileName="$targetPath$fileName"

#echo "$linkFileName"
rm -v -f "$linkFileName"

#echo "$targetFileName" "$linkFileName"
ln -v -s "$targetFileName" "$linkFileName"

#pause
read -n1 -r -s
