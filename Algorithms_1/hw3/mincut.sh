#! /bin/sh

# invoke mincut.py everytime

i=0
min=500
while [ $i -lt 50 ]; do
	instance=$(./mincut.py)
	if [ $instance -lt $min ]; then
		min=$instance
	fi
	i=$(($i + 1))
done
echo "I am done. Min is $min"
