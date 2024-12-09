#! /bin/sh
cat ./dictionary/sorted.tsv > ./dictionary/dictionary.tsv
pandoc -s -o ./html/dictionary.html ./dictionary/dictionary.tsv --metadata title="Qʼathebʼo Dictionary"
