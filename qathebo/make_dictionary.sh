#! /bin/sh
cat ./dictionary/sorted.tsv > ./dictionary/dictionary.tsv
pandoc -t html ./dictionary/dictionary.tsv | cat <(echo "<style>") ./html/dictionary.css <(echo "</style>") - | pandoc -s -o ./html/dictionary.html --metadata-file="./metadata/dictionary.yaml"
