#! /bin/sh
cut ./dictionary/raw.tsv -f 2 | tail --lines=+2 > ./lexicon/dict_raw.wli
lexurgy sc -o modern ./lexicon/lex.lsc ./lexicon/dict_raw.wli
rename raw_modern modern ./lexicon/dict_raw_modern.wl*
lexurgy sc -o adlam ./lexicon/adlam.lsc ./lexicon/dict_modern.wli
rename modern_adlam adlam ./lexicon/dict_modern_adlam.wl*
paste ./lexicon/dict_adlam.wli ./lexicon/dict_modern.wli | cat <(paste <(echo "Adlam") <(echo "Phonetic")) - | paste - <(cut -f 3-5 ./dictionary/raw.tsv) > ./dictionary/adlam.tsv
sort ./dictionary/adlam.tsv > ./dictionary/sorted.tsv
