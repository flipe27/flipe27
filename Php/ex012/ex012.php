<?php 
    // 'isset()' checa se foi informado parâmetro para '$_GET[]'
    $nome = isset($_GET['nome']) ? $_GET['nome'] : 'Não informado';
    $ano = isset($_GET['ano']) ? $_GET['ano'] : 0;
    $sexo = isset($_GET['sexo']) ? $_GET['sexo'] : '[sem sexo]';
    $idade = date('Y') - $ano;
    
    echo "$nome é $sexo e tem $idade anos"
?>