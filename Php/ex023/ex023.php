<?php 
    $valor = $_GET['val'];
    $fatorial = 1;
    $cont = $valor;

    echo "$valor! = ";
    do {
        if($cont == 1) {
            echo $cont . ' ';
        } else {
            echo $cont . ' x ';
        }
        $fatorial *= $cont;
        $cont--;
    } while($cont >= 1);

    echo "= $fatorial";
?>
