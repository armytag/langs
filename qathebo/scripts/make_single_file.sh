#! /bin/sh
cat <(echo "<style>") $LANG_CSS_FILE <(echo "</style>") $LANG_MD_FILE | pandoc -s --toc -o $LANG_OUTPUT_FILE
