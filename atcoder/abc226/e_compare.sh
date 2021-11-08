#!/bin/bash

cnt=0
while true; do
    cnt=$(( $cnt + 1 ))
    python e_input.py > input.txt
    python e_naive.py < input.txt > out1.txt
    python e.py       < input.txt > out2.txt

    echo "--- Test $cnt ---"
    cat input.txt
    df=$(diff out1.txt out2.txt)
    if [ -n "$df" ]; then
        echo "Naive answer is ..."
        cat out1.txt
        echo "Faster answer is ..."
        cat out2.txt
        exit
    fi
done
