if [ $# -eq 0 ]
then
	message="lazy git commit"
else
	message="$1"
fi

git add .
git commit -m "$message"
git push