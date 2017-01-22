#!/bin/bash

#  Dieses script führt alle Python und Bash-Scripte im selben Ordner
#  aus, die mit einer Ziffer beginnen und auf .py oder .sh und auch alle Scratch Programme
#  mit der Endung sb aus.

#  Um ein Script zu deaktivieren, muss lediglich die führende
#  Zahl entfernt werden.

cd $(dirname $0)

for i in [0-9]*.{py,sh}; do
	if [ -e $i ] && [ ${i##*.} == 'py' ]; then
		python "$i" > $i.log &
	elif [ -e $i ] && [ ${i##*.} == 'sh' ]; then
		./$i > $i.log &
    elfif [ -e $i ] && [ ${i##*.} == 'sb' ]; then
        scratch presentation "$i"  > $i.log &
	fi
done
