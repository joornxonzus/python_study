y=$(date +%y)
m=$(date +%m)
d=$(date +%d)
H=$(date +%H)
M=$(date +%M)
S=$(date +%S)
git add .
git commit -m "
$y/$m/$d-$H:$M:$S 
更新python的基础知识，最基本结束
Signed-off-by: LeeBin 
<hest0001@163.com>"
git push origin master
