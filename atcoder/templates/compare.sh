#!/bin/bash -eu

cnt=0
while true; do
    cnt=$(( $cnt + 1 ))
    python problem_no_input.py > input.txt
    python problem_no_naive.py < input.txt > out1.txt
    python problem_no.py       < input.txt > out2.txt

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
