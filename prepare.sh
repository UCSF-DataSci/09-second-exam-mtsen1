#!/bin/bash

python3 generate_dirty_data.py

input_file="ms_data_dirty.csv"
output_file="ms_data.csv"
insurance_file="insurance.lst"

# removing comments, empty lines, and extra commas
cleaned_data=$(grep -v '^#' "$input_file" | sed '/^$/d' | sed 's/,,*/,/g')

# keeping only the essential columns
essential_columns=$(echo "$cleaned_data" | cut -d',' -f1,2,4,5,6)

# keeping only rows with valid walking speeks
valid_data=$(echo "$essential_columns" | awk -F',' 'NR==1 || ($5 >= 2.0 && $5 <= 8.0)')

echo "$valid_data" > "$output_file"

# making insurance file
cat <<EOL > "$insurance_file"
insurance_type
Basic
Premium
Platinum
EOL

# Summary of the cleaned data
total_visits=$(echo "$valid_data" | wc -l)

let "total_visits-=1"

echo "Summary of the cleaned data:"
echo "Total number of visits: $total_visits"
echo "First few records:"
echo "$valid_data" | head -n 5