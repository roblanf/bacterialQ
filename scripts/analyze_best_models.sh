#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <best_scheme.nex> <output_file>"
  exit 1
fi

best_scheme_file=$1
output_file=$2

if [ ! -f $best_scheme_file ]; then
  echo "File $best_scheme_file does not exist"
  exit 1
fi

grep '^ *[^ ]\+:' $best_scheme_file | awk -F: '{print $1}' | awk '{print $NF}' | cut -d'+' -f1 | sort | uniq -c | sort -nr > $output_file

best_model=$(head -n 1 $output_file | awk '{print $2}')
echo -n $best_model