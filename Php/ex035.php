<pre>
<?php 
    $n = array(3, 5, 8, 2);
    $n[] = 7;
    print_r($n);

    $c = range(5, 20, 2);
    print_r($c);

    foreach($c as $valor) {
        echo "$valor ";
    }

    $v = array(1 => 'A', 3 => 'B', 5 => 'C', 7 => 'D');
    echo "<br>";
    $v[] = 'E';
    unset($v[8]);
    print_r($v);
?>
</pre>
