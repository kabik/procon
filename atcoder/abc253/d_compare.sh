#!/bin/bash

cnt=0
while true; do
    echo "--- Test $cnt ---"
    cnt=$(( $cnt + 1 ))
    python3 d_input.py > input.txt
    python3 d_naive.py < input.txt > out1.txt
    python3 d.py       < input.txt > out2.txt

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
