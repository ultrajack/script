#!/bin/sh

if [ "$1" == "" ]; then
  echo "Usage: $0 <listfile>"
  exit 1
fi

for f in `cat $1`
do
  echo $f
  ./createClassifier.py $f
done
