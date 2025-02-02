#!/bin/zsh
CYDATE=$(date -d "2024-1-1 +$(($1 - 1)) days" +%F)
CYSLASHED=$(echo $CYDATE | sed 's/-/\//g')
CYEXPANDED=$(date -d $CYDATE +%B-%-d-%Y)
echo "https://www.quothalinguist.com/$CYSLASHED/day-$1-$CYEXPANDED/"
