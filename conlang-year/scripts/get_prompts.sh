#!/bin/zsh
for i in `seq 1 366`; do
	echo "Getting day $i"
	./prompt_html.sh $i > ../prompts/$i.html
done
