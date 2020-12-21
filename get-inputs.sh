#!/bin/bash
# name: Amirhossein Alibakhsi 
# id: 9731096
if [ $# -eq 0 ]
then
 echo $# inputs\(s\) were inserted...
fi

if [ $# -eq 1 ]
then
 c=0
 sum=0
 while [ $c -le $1 ]
 do
  ((sum=sum+c))
  ((c++))
 done
 echo sum is $sum
fi

if [ $# -eq 2 ]
then
 let sum=$1+$2
 echo $1 + $2 \= $sum
fi
