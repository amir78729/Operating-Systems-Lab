#!/bin/bash
# Amirhossein
# Alibakhshi
# 9731096
myfunction() {
 local local_variable="LOCAL_FUNCTION"
 global_variable="GLOBAL_FUNCTION"
 echo "    > $local_variable"
 echo "    > $global_variable"
 echo "    > USING FOR LOOP TO PRINT ARRAY"
 for i in $array
 do
  echo "       > $i"
 done
}

echo " > INSERT SOME INPUTS, THEN PRESS ENTER"
read array
local_variable="LOCAL"
global_variable="GLOBAL"
echo " > START"
echo "    > $local_variable"
echo "    > $global_variable"
echo ''
echo " > FUNCTION CALLED"
myfunction
echo ''
echo " > AFTER THE FUNCTION"
echo "    > $local_variable"
echo "    > $global_variable"
