#! /bin/sh
cat <(echo "<style>") style/template.css <(echo "</style>") texts/cdn_winter_relay.md | pandoc -s --toc -o texts/cdn_winter_relay.html --metadata title="Qʼathebʼo Torch - CDN Winter Relay"
