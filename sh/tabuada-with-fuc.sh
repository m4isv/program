clear


function maiuscula(){
    echo $1 | tr a-z A-Z

}


RESULT=$(maiuscula ola)

echo "$RESULT"

