<?php 
    function teste(&$x) {  // Com o '&' antes do parâmetro, o que acontecer com $x vai acontecer com $a
        $x += 2;
        echo "O valor de x é $x";
    }

    $a = 3;
    teste($a);
    echo "<br>O valor de a é $a";
?>
