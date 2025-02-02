#!/bin/zsh
for i in `seq 1 366`; do
	echo "Updating day $i"
	echo "<link href='prompt.css' rel='stylesheet'>" >>../prompts/$i.html
done
