
#!/bin/bash
# Amirhossein
# Alibakhshi
# 9731096
if (($#!=3))
then
 echo Please enter a correct format\!
 echo Here are some allowed examples:
 echo + 1 2
 echo - 9 6
 echo \* 5 8
 echo / 28 7
 echo ADD 1 2
 echo SUB 9 6
 echo MUL 5 8
 echo DIV 28 7
else # 3 inputs are inserted.
 op=$1
 a=$2
 b=$3
 res=0
 case $op in
  + | add | ADD )
   ((res=a+b))
   echo $a + $b = $res
   ;;
  - | sub | SUB )
   ((res=a-b))
   echo $a - $b = $res
   ;;
  \* | mul | MUL )
   ((res=a*b))
   echo $a * $b = $res
   ;;
  / | div | DIV )
   ((res=a/b))
   if ((b==0))
    then
     echo Division by ZERO error!
    else
     echo $a / $b = $res
   fi
   ;;
  *)
   echo \"$op\" is not a supported operand.
   ;;
 esac
fi
