#! /bin/sh
cat <(echo "<style>") ./style/template.css <(echo "</style>") ./notes.md | pandoc -s --toc -N -o ./html/notes.html --metadata-file="./metadata/notes.yaml"
