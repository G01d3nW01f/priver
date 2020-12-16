echo Priver installer

sudo apt update -y

sudo apt update cython3 -y

cython3 priver.py --embed -o priver.c --verbose

if [ $? -eq 0 ]; then
    echo [SUCCESS] Generated C code
else
    echo [ERROR] Build failed. Unable to generate C code using cython3
    exit 1

fi

gcc -Os -I /usr/include/python3.8 -o priver priver.c -lpython3.8 -lpthread -lm -lutil -ldl
if [ $? -eq 0 ]; then
    echo [SUCCESS] Compiled to static binay
   

else
    echo [ERROR] Build failed
    exit 1
