#!/bin/bash -eu

cnt=0
while true; do
    cnt=$(( $cnt + 1 ))
    python d_input.py > input.txt
    a1=$(python d_naive.py < input.txt)
    a2=$(python d.py < input.txt)

    echo "--- Test $cnt ---"
    cat input.txt
    if [ $a1 != $a2 ]; then
        echo "Naive answer is ..."
        echo $a1
        echo "Faster answer is ..."
        echo $a2
        exit
    fi
done
