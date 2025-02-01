#! /bin/sh
cat <(echo "<style>") style/template.css <(echo "</style>") texts/cdn_winter_relay.md | pandoc -s --toc -o texts/temp.html --metadata title="Qʼathebʼo Torch - CDN Winter Relay"
awk -f ./generate_numbered_glosses.awk ./texts/temp.html > ./texts/cdn_winter_relay.html
rm ./texts/temp.html
