#! /bin/sh
cat <(echo "<style>") ./style/template.css <(echo "</style>") ./grammar/introduction.md ./grammar/phonology.md ./grammar/nouns.md ./grammar/pronouns.md ./grammar/verbs.md ./grammar/adverbs.md ./grammar/modifiers.md ./grammar/syntax.md ./grammar/discourse.md ./grammar/examples.md ./grammar/appendices.md | pandoc -s --toc -N -o ./html/temp.html --metadata-file="./metadata/grammar.yaml"
awk -f ./generate_numbered_glosses.awk ./html/temp.html > ./html/grammar.html
rm ./html/temp.html
