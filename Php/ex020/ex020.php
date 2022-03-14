<?php 
    $i = 1;
    while($i <= 5) {
        $v = 'num' . $i;
        $url = 'v' . $i;
        $$v = isset($_GET[$url]) ? $_GET[$url] : 0;
        $i++;
    }
    $i = 1;
    while($i <= 5) {
        $v = 'num' . $i;
        echo "Volor $i: " . $$v . "<br>";
        $i++;
    }
?>