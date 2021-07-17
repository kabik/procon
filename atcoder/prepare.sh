#!/bin/bash

no=$1
prefix="abc"
problems=("a" "b" "c" "d" "e" "f")
template_file="template.py"
random_input_file="random_input.py"
compare_file="compare.sh"

if [ -z "$no" ]; then
    echo "usage: ./abc_py.sh problem_no"
    exit 0
fi

for i in ${problems[@]}; do
    prob_dir=${prefix}${no}
    mkdir -p ${prob_dir}
    cp -i $template_file ${prob_dir}/${i}.py
    cp -i $template_file ${prob_dir}/${i}_naive.py
    cp -i $random_input_file ${prob_dir}/${i}_input.py
    sed -e "s/problem_no/${i}/g" $compare_file > ${prob_dir}/${i}_compare.sh
done
cp -i $template_file ${prob_dir}/tmp.py
