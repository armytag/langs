#! /bin/sh
cat <(echo "<style>") ./style/template.css <(echo "</style>") ./grammar/introduction.md ./grammar/phonology.md ./grammar/morphology.md ./grammar/derivation.md ./grammar/syntax.md ./grammar/discourse.md ./grammar/examples.md ./grammar/appendices.md | pandoc -s --toc -N -o ./html/grammar.html --metadata-file="./metadata/grammar.yaml"
