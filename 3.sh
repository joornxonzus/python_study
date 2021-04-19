dt=$(date +%m%d)
dt2=$(date +%H%M)
git add .
git commit -m "$dt-$dt2 Signed-off-by: LeeBin <hest0001@163.com>"
git push origin master