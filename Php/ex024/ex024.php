<?php 
    $num = $_GET['num'];
    $cont = 1;

    echo "Mostrando a tabuada de $num<br>";

    do {
        echo "$num x $cont = " . ($num * $cont) . "<br>";
        $cont++;
    } while($cont <= 10);
?>
