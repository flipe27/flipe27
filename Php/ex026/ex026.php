<?php 
    $num = $_GET['num'];

    echo "Mostrando a tabuada de $num<br>";
    
    for($c = 1; $c <= 10; $c++) {
        echo "$num x $c = " . ($num * $c) . "<br>";
    }
?>