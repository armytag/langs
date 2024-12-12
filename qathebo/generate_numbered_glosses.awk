BEGIN {
	id=1;
}

{
	numberline = match($0, /class=.number./)
	if (numberline != 0) {
		print "<p class=\"number\">" id "</p>"
		id++
	} else {
		print $0
	}
}

END {}
