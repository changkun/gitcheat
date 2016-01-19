int=1
while(( $int<=30 ))
do
        echo $int > 1.txt
        git add 1.txt
        git commit --date=2015-11-$int -m "wow?"
        let "int++"
done
