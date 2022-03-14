<?php 
    $estado = $_GET['estado'];

    switch($estado) {
        case '1':
            $r = 'Região Norte';
            break;
        case '2':
            $r = 'Região Nordeste';
            break;
        case '3':
            $r = 'Região Sul';
            break;
        case '4':
            $r = 'Região Sudeste';
            break;
        default:
            $r = 'Região Centro-Oeste';
    }

    echo "Você mora na <span id='cor'>". $r. "</span>";
?>

<style>
    #cor {
        color: red;
    }
</style>
