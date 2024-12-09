#! /bin/sh
cat ./dictionary/sorted.tsv > ./dictionary/dictionary.tsv
cut -f 1-4 ./dictionary/dictionary.tsv | pandoc -f tsv -t html | cat <(echo "<style>") ./html/dictionary.css <(echo "</style>") - | pandoc -s -o ./html/dictionary.html --metadata-file="./metadata/dictionary.yaml"
