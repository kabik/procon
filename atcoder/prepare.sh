#!/bin/bash -eu

no=$1
prefix="abc"
problems=("a" "b" "c" "d" "e" "f")
src_dir="templates"
template_py="template.py"
random_input_src="random_input.py"
compare_src="compare.sh"

if [ -z "$no" ]; then
    echo "usage: ./abc_py.sh problem_no"
    exit 0
fi

# Base directory
prob_dir=${prefix}${no}
mkdir -p ${prob_dir}

# Rust
mkdir -p ${prob_dir}/rust/src/bin
cp -i ${src_dir}/rust/Cargo.{toml,lock} ${prob_dir}/rust/
cp -ir ${src_dir}/rust/target ${prob_dir}/rust/target

for i in ${problems[@]}; do
    # Python
    cp -i ${src_dir}/${template_py} ${prob_dir}/${i}.py

    # Rust
    cp -i ${src_dir}/rust/src/bin/template.rs ${prob_dir}/rust/src/bin/${i}.rs

    # Utilities
    cp -i ${src_dir}/${template_py}      ${prob_dir}/${i}_naive.py
    cp -i ${src_dir}/${random_input_src} ${prob_dir}/${i}_input.py
    cp -i ${src_dir}/${compare_src}      ${prob_dir}/${i}_compare.sh
    sed -i'.bk' -e "s|problem_no|${i}|g" ${prob_dir}/${i}_compare.sh
    rm ${prob_dir}/${i}_compare.sh.bk
done
cp -i ${src_dir}/${template_py} ${prob_dir}/tmp.py
