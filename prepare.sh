#!/bin/bash

no=$1
prefix="abc"
problems=("a" "b" "c" "d" "e" "f")
template_file="template.py"

if [ -z "$no" ]; then
    echo "usage: ./abc_py.sh problem_no"
    exit 0
fi

for i in ${problems[@]}; do
    prob_dir=${prefix}${no}
    mkdir -p ${prob_dir}
    cp -i $template_file ${prob_dir}/${i}.py
    touch ${prob_dir}/${input_file}
done
