<?php 
    $dia = $_GET['dia'];

    switch($dia) {
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            echo 'Levanta e vai estudar :)';   
            break;
        case 7:
        case 1:
            echo 'Dia de descansar!';    
            break;
        default:
            echo 'Dia da semana inválido';
    }
?>