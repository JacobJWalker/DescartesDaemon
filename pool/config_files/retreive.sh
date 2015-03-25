#!/bin/bash

# filename variablename datainfo $3
# bash /cdrom/pool/config_files/declare.sh VirtualImageURL $VirtualImageURL $3
# Fun fact, this doesn't need bash to work... Which means this is going to leave us soon

################# WHEN LOADING UP AT FIRST #####################
NumberOfVMs=$3
eval variableName="$1_$(printf %04g $NumberOfVMs)"
variableVal="$2_$(printf %04g $NumberOfVMs)"
eval ${variableName}=`echo -ne \""${variableVal}"\"`
eval "echo \$${variableName}" > "$1_$(printf %04g $NumberOfVMs)"


################### WHEN LOADING LATER #####################

#test=`cat "$1_$(printf %04g $NumberOfVMs)"`
#echo $test