git add .
echo "Enter a commit message"
read message
git commit -m "$message" 
git remote add origin https://github.com/zackkattack/-CS1411.git
git push origin master
