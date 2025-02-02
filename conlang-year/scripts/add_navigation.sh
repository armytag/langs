#!/bin/zsh
for i in `seq 1 366`; do
	echo "Updating day $i"
	# echo "<div class='nav'>" >>../prompts/$i.html
	# if [[ $i -gt 1 ]]; then
	# 	echo "<a href='$(($i - 1)).html'>Day $(($i - 1))</a>" >>../prompts/$i.html
	# fi
	# if [[ $i -lt 366 ]]; then
	# 	echo "<a href='$(($i + 1)).html'>Day $(($i + 1))</a>" >>../prompts/$i.html
	# fi
	# echo "</div>" >>../prompts/$i.html
done
