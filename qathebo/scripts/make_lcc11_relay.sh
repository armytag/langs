#! /bin/sh
cat <(echo "<style>") style/template.css <(echo "</style>") texts/LCC11_Gloss.md | pandoc -s --toc -o texts/temp.html --metadata title="Qʼathebʼo Torch - LCC11 Relay"
awk -f ./generate_numbered_glosses.awk ./texts/temp.html > ./texts/lcc11_relay.html
rm ./texts/temp.html
