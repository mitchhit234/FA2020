#!/bin/bash

full=$1
filename=$(echo "${full%.*}")

pdflatex -halt-on-error $1

rm "${filename}.aux"
rm "${filename}.log"
rm "${filename}.out"