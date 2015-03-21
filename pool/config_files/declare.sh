export NumberOfVMs=`cat /variables/NumberOfVMs`
export $1=`cat /variables/$1`
declare $1_$(printf %04g $NumberOfVMs)=$1
echo $1_$(printf %04g $NumberOfVMs) > /variables/$1_$(printf %04g $NumberOfVMs)