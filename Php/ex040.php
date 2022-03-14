<pre>
    <?php 
        $v = array('A', 'K', 'M', 'X', 'B');
        print_r($v);
        sort($v);
        print_r($v);
        rsort($v);
        print_r($v);
        // As funções 'asort()' e 'arsort()' também ordenam os vetores, porém alterando também a posição dos seus índices
        // As funções 'ksort()' e 'krsort()' ordenam o vetor a partir dos índices
    ?>
</pre>
