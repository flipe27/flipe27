<?php 
    $valor = $_GET['value'];
    $raiz = sqrt($valor);
    echo "A raíz de $valor é igual a ". number_format($raiz, 2);
?>