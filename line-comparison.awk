#! /usr/bin/awk -f
BEGIN {prev = 738}
$1 > prev + 1 {print prev + 1, "skipped"} $1 < prev + 1 {print $1, "duplicated"} {prev = $1}
