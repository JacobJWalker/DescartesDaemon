export NumberOfVMs=`cat /variables/NumberOfVMs`
if [ -z "$2" ]; then
	:
else
	NumberOfVMs=$2
fi
declare $1_$(printf %04g $NumberOfVMs)=$1
echo $1_$(printf %04g $NumberOfVMs) > /variables/$1_$(printf %04g $NumberOfVMs)