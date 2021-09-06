#!/bin/bash 

file="paths.txt"
clear
read -p 'Enter Website Url : ' web


while read line; do
total=$web$line
brute=$(curl -o /dev/null --silent --head --write-out '%{http_code}\n' $total)
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

