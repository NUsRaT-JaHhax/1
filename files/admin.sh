#!/bin/bash

file="paths.txt"
clear
read -p 'Enter Website Url : ' web


while read line; do
total=$web$line
brute=$(curl --head --max-time 0.5 -s -o /dev/null \
                      -w "%{http_code} %{time_total} %{url_effective}\n" \
                      $total | awk '{print $1}'
)
if [ $brute = "200" ];
then
echo "FOUND : $total"
elif [ $brute = "302" ];
then
echo "FOUND : $total"
else
echo "NOT FOUND : $total"
fi
done < $file
