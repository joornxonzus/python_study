day=$(date +%m%d)
tim=$(date +%H%M)
note=$("linux")
git add .
git commit -m "$day-$tim:$note Signed-off-by: LeeBin <hest0001@163.com>"
git push origin master