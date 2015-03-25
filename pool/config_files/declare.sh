#!/bin/bash

# filename variablename datainfo $NumberOfVMs
# bash /cdrom/pool/config_files/declare.sh VirtualImageURL $VirtualImageURL $NumberOfVMs
# Fun fact, this doesn't need bash to work... Which means this is going to leave us soon

NumberOfVMs=$3
variableName="$1_$(printf %04g $NumberOfVMs)"
variableVal="$2"
eval ${variableName}=`echo -ne \""${variableVal}"\"`
echo $variableVal > /variables/${variableName}