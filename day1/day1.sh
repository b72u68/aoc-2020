#!/bin/sh

declare -a data
data=(`cat "data.txt" | sort -n`)

while IFS= read -r line; do
    if grep -Fxq "$((2020 - $line))" data.txt; then
        echo $(($((2020 - $line)) * $line))
        break
    fi
done < data.txt

for ((i=0; i < $((${#data[@]}-2)); i++)); do
    for ((j=i+1; j < $((${#data[@]}-1)); j++)); do
        for ((k=j+1; k < $((${#data[@]})); k++)); do
            s=$((data[$i] + data[$j] + data[$k]))
            if [[ $s -gt 2020 ]]; then
                break
            elif [[ $s -eq 2020 ]]; then
                echo $((data[$i] * data[$j] * data[$k]))
                break
            fi
        done
    done
done
