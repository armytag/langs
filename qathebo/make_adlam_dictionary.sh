#! /bin/sh
cut ./dictionary/unsorted_dictionary.tsv -f 2 | tail --lines=+2 > ./lexicon/dict.wli
lexurgy sc -o adlam ./lexicon/adlam.lsc ./lexicon/dict.wli
cat <(echo "Adlam") ./lexicon/dict_adlam.wli | paste - <(cut -f 2-5 ./dictionary/unsorted_dictionary.tsv) > ./dictionary/auto_adlam.tsv
sort ./dictionary/auto_adlam.tsv > ./dictionary/sorted_dictionary.tsv
