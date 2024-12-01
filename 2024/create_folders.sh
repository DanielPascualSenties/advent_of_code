#!/bin/bash

start=10
end=24
for((i=$start;i<=$end;i++))
do
mkdir "day${i}"
cd day${i}
touch day${i}_input.txt
touch day${i}_example.txt
touch day${i}.py
touch day${i}_tests.py
cd ..
done