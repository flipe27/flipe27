<?php 
    $num = $_GET['num'];
    $op = $_GET['op'];

    switch($op){
        case '1':
            $res = $num * 2;
            break;
        case '2':
            $res = pow($num, 3);
            break;
        default:
            $res = sqrt($num);
    }

    echo "O resultado da operação é $res";
?>