<?php 
    $ano = $_GET['ano'];
    $idade = date('Y') - $ano;

    echo "Você nasceu em $ano e tem $idade anos";
    
    if($idade < 16) {
        $v = 'você não pode votar';
    }
    elseif(($idade >= 16 and $idade < 18) or $idade > 65) {
        $v = 'seu voto é opcional';
    } else {
        $v = 'seu voto é obrigatório';
    }

    echo "<br>Com essa idade $v";
?>