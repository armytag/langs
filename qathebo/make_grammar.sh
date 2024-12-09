#! /bin/sh
pandoc -s --toc -N -o ./html/grammar.html ./grammar/introduction.md ./grammar/phonology.md ./grammar/morphology.md ./grammar/derivation.md ./grammar/syntax.md ./grammar/discourse.md ./grammar/examples.md ./grammar/appendices.md ./metadata/grammar.yaml
