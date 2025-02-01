#! /bin/sh
cat <(echo "<style>") style/template.css <(echo "</style>") index.md | pandoc -s --toc -o html/index.html --metadata title="Qʼathebʼo Index Page"
