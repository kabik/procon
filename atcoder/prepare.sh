#!/bin/bash -eu

no=$1
prefix="abc"
problems=("a" "b" "c" "d" "e" "f")
src_dir="templates"
template_src="template.py"
random_input_src="random_input.py"
compare_src="compare.sh"

if [ -z "$no" ]; then
    echo "usage: ./abc_py.sh problem_no"
    exit 0
fi

for i in ${problems[@]}; do
    prob_dir=${prefix}${no}
    mkdir -p ${prob_dir}
    cp -i ${src_dir}/${template_src} ${prob_dir}/${i}.py
    cp -i ${src_dir}/${template_src} ${prob_dir}/${i}_naive.py
    cp -i ${src_dir}/${random_input_src} ${prob_dir}/${i}_input.py
    cp -i ${src_dir}/${compare_src} ${prob_dir}/${i}_compare.sh
    sed -i'.bk' -e "s|problem_no|${i}|g" ${prob_dir}/${i}_compare.sh
    rm ${prob_dir}/${i}_compare.sh.bk
done
cp -i ${src_dir}/${template_src} ${prob_dir}/tmp.py
