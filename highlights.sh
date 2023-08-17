#!/usr/bin/env bash
cd /home/raahi/YTapi/youtube-api
tdnice=`date +"%B %d, %Y"`
td=`date +"%Y%m%d"`

source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:/home/raahi/YTapi/pytube
python main.py

filename=videos/edited/${td}_highlights.mp4

python uploading.py --file $filename --title "Popular on YouTube Highlights: $tdnice" --description "`cat $desc_path`" --privacyStatus public
