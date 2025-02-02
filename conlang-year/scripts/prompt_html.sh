#!/bin/zsh
./prompt_url.sh $1 | xargs curl -s | pup "h1, .entry-content > div, .entry-content > p"
