#!/bin/bash

no=$1
prefix="abc"
problems=("a" "b" "c")
template_file="template.cc"
main_file="main.cc"

if [ -z "$no" ]; then
    echo "usage: ./abc_cpp.sh problem_no"
    exit 0
fi

for i in ${problems[@]}; do
    prob_dir=${prefix}${no}/${i}
    mkdir -p ${prob_dir}
    cp -i $template_file ${prob_dir}/${main_file}
    touch ${prob_dir}/${input_file}
done
