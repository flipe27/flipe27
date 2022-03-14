<?php 
    function soma() {
        $p = func_get_args();
        $tot = func_num_args();
        $r = 0;

        for($i = 0; $i < $tot; $i++) {
            $r += $p[$i];
        }
        return $r;
    }

    $res = soma(1, 2, 3, 4, 5);
    echo "A soma dos valores é $res";
?>
