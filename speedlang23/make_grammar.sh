#! /bin/sh
METADATA_DATE=$(date +"%-d %B %Y")
sed -i "/^date/c\date: '$METADATA_DATE'" ./metadata_grammar.yaml
cat <(echo "<style>") ./template.css <(echo "</style>") ./grammar.md | pandoc -s -o ./temp.html --metadata-file="./metadata_grammar.yaml"
awk -f ./generate_numbered_glosses.awk ./temp.html > ./grammar.html
rm ./temp.html
