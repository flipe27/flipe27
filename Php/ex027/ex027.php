<?php 
    $num = $_GET['num'];
    $primo = 0;
    $res = '';

    for($cont = 1; $cont <= $num; $cont++) {
        if($num % $cont == 0) {
            $primo++;
            $mult .= $cont . ' ';
        }
    }

    if($primo > 2) {
        $p = 'não é primo!';
    } else {
        $p = 'é primo!';
    }

    echo "Analisando o número $num...<br>";
    echo "Valores múltiplos: $mult<br>";
    echo "Total de múltiplos: $primo<br>";
    echo "Resultado: $num <span id='res'>$p</span>";
?>

<style>
    #res {
        color: red;
    }
</style>
