#!/bin/bash

cnt=0
while true; do
    echo "--- Test $cnt ---"
    cnt=$(( $cnt + 1 ))
    python3 c_input.py > input.txt
    python3 c_naive.py < input.txt > out1.txt
    python3 c.py       < input.txt > out2.txt

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
