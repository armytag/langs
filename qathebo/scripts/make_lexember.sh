#! /bin/sh
cat <(echo "<style>") ./style/template.css <(echo "</style>") ./lexicon/lexember2024.md | pandoc -s --toc -o ./html/lexember.html --metadata-file="./metadata/lexember.yaml"
