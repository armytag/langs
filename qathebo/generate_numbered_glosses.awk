BEGIN {
	id=0;
}

{
	modified = 0
	reference = match($0, /%{[\+-][0-9]}%/)
	if (reference != 0) {
		split($0, splits, " ")
		for (sp in splits) {
			relative = match(splits[sp], /%{([\+-][0-9]+)}%/, refs)
			if (relative != 0) {
				rel_num = int(refs[1])
				ref_num = id + rel_num
				if (rel_num < 0) {
					ref_num++
				}
				print "(" ref_num ")"
			} else {
				print splits[sp]
			}
		}
		modified = 1
	}
	numberline = match($0, /^<p class=.number./)
	if (numberline != 0) {
		id++
		print "<p class=\"number\">" id "</p>"
		modified = 1
	}
	if (modified == 0) {
		print $0
	}
}

END {}
