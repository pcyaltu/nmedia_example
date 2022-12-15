if [ $# -eq 0 ] ; then
    folder=`ls *.txt`
else
    folder=`ls $1`
fi


for f in ${folder}; do

    name=`basename ${f} .txt`
    echo ${name}

done