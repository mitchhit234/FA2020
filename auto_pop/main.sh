#!/bin/bash
shopt -s expand_aliases

script_location="/home/mitchhit234/scripts/auto_pop/"

ext=$(echo $1 | sed 's/.*\.//')
editor="$2"
populate="${script_location}template.${ext}"

{
	cp $populate $1
} || {
	echo "No template avaliable for $ext files"
	exit 0
}

$2 $1