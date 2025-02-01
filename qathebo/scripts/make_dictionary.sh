#! /bin/sh
cat ./dictionary/sorted.tsv > ./dictionary/dictionary.tsv
cut -f 1-4 ./dictionary/dictionary.tsv | pandoc -f tsv -t html | cat <(echo "<style>") ./style/dictionary.css <(echo "</style>") - | pandoc -s -o ./html/dictionary.html --metadata-file="./metadata/dictionary.yaml"
cat ./dictionary/sorted.tsv > ./dictionary/raw.tsv
