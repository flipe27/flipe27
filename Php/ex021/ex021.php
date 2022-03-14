<?php 
    $inicio = (int) $_GET['i'];
    $final = (int) $_GET['f'];
    $passo = (int) $_GET['cont'];

    if($final > $inicio) {
        while($inicio <= $final) {
            echo $inicio . " ";
            $inicio += $passo;
        }
    } else {
        while($final <= $inicio) {
            echo $inicio . " ";
            $inicio -= $passo;
        }
    }
?>
