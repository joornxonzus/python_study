day=$(date +%m%d)
tim=$(date +%H%M)
git add .
git commit -m "$day-$tim: 
				Signed-off-by: LeeBin <hest0001@163.com>"
git push origin master