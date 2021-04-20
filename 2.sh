y=$(date +%y)
m=$(date +%m)
d=$(date +%d)
H=$(date +%H)
M=$(date +%M)
S=$(date +%S)
git add .
git commit -m "
python基础
$y/$m/$d-$H:$M:$S 
Signed-off-by: LeeBin 
<hest0001@163.com>"
git push origin master
