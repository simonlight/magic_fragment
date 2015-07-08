function walk()  
{  
  for file in `ls $1`  
  do  
    local path=$1"/"$file  
    if [ -d $path ]  
     then  
      echo "DIR $path"  
      walk $path  
    else  
      echo "FILE $path"
	  #convert $path $path  
    fi  
  done  
}  

if [ $# -ne 1 ]  
then  
  echo "USAGE: $0 TOP_DIR"  
else  
  walk $1  
fi 


