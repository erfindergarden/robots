#!/bin/bash

#  Dieses script führt alle Python und Bash-Scripte im selben Ordner
#  aus, die mit einer Ziffer beginnen und auf .py oder .sh enden.
#
#  Um ein Script zu deaktivieren, muss lediglich die führende
#  Zahl entfernt werden.

cd $(dirname $0)

for i in [0-9]*.{py,sh}; do
	if [ -e $i ] && [ ${i##*.} == 'py' ]; then
		python "$i" &
	elif [ -e $i ] && [ ${i##*.} == 'sh' ]; then
		./$i &
	fi
done
