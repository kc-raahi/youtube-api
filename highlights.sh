#!/usr/bin/env bash
$tdnice=date +"%B %d, %Y"
$td=date +"%Y%m%d"

$env:PYTHONPATH="C:\Users\klarc\PycharmProjects\pytube"
.\venv\Scripts\activate.ps1

python .\main.py

$filename="videos\edited\"+$td+"_highlights.mp4"
$title="Popular on YouTube Highlights: "+$tdnice
$desc_path=".\data\"+$td+"_highlights.txt"
$desc=`cat $desc_path

python .\uploading.py --file $filename --title $title --description $desc --privacyStatus public