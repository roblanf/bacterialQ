#!/bin/bash

train_loc_path="$1"
test_loc_path="$2"
loci_list="$3"
taxa_list="$4"
output_dir="$5"

train_loci_dir="$output_dir/loci/training_loci"
test_loci_dir="$output_dir/loci/testing_loci"

mkdir -p $train_loci_dir
mkdir -p $test_loci_dir

if [ -s "$loci_list" ]; then
  train_loci_files=$(grep -Fxf "$loci_list" <(find "$train_loc_path" -type f -iname "*.fa*" -printf "%f\n"))
  test_loci_files=$(grep -Fxf "$loci_list" <(find "$test_loc_path" -type f -iname "*.fa*" -printf "%f\n"))
else
  train_loci_files=$(find "$train_loc_path" -type f -iname "*.fa*" -printf "%f\n")
  test_loci_files=$(find "$test_loc_path" -type f -iname "*.fa*" -printf "%f\n")
fi

if [ -z "$train_loci_files" ] || [ -z "$test_loci_files" ]; then
  echo "Training or testing loci set is empty after filtering. Program will terminate."
  exit 1
fi

echo "Number of training loci: $(echo $train_loci_files | wc -w)"
echo "Number of testing loci: $(echo $test_loci_files | wc -w)"

check_empty_seq() {
  local file_path="$1"
  if grep -q -E '^[>-?]+$' "$file_path"; then
    return 0
  else
    return 1
  fi
}

run_faSomeRecords() {
  local loci_files="$1"
  local taxa_list="$2"
  local output_dir="$3"
  
  if [ -f "$taxa_list" ]; then
    for file in $loci_files; do
      file_path=$(find "$train_loc_path" -type f -iname "$file")
      output_file="$output_dir/$file"
      faSomeRecords "$file_path" "$taxa_list" "$output_file"
      if check_empty_seq "$output_file"; then
        rm "$output_file"
        echo "Removed empty sequence file: $output_file"
      fi
    done
  elif [ -d "$taxa_list" ]; then
    for tree_file in "$taxa_list"/*.txt; do
      tree_name=$(basename "$tree_file" .txt)
      for file in $loci_files; do
        file_path=$(find "$train_loc_path" -type f -iname "$file")
        loci_name=$(basename "$file" | cut -d. -f1)
        ext=$(basename "$file" | cut -d. -f2-)
        output_file="$output_dir/${tree_name}_${loci_name}.${ext}"
        faSomeRecords "$file_path" "$tree_file" "$output_file"
        if check_empty_seq "$output_file"; then
          rm "$output_file"
          echo "Removed empty sequence file: $output_file"
        fi
      done
    done
  else
    echo "$taxa_list is neither a file nor a directory."
    exit 1
  fi
}

run_faSomeRecords "$train_loci_files" "$taxa_list" "$train_loci_dir"
run_faSomeRecords "$test_loci_files" "$taxa_list" "$test_loci_dir"

echo "Finished splitting alignments"