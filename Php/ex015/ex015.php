<?php 
    $n1 = $_GET['n1'];
    $n2 = $_GET['n2'];
    $media = ($n1 + $n2) / 2;

    if($media >= 0 and $media < 5) {
        $sit = 'REPROVADO';
    } 
    elseif($media >= 5 and $media < 7) {
        $sit = 'EM RECUPERAÇÂO';
    }   
    else {
        $sit = 'APROVADO';
    }

    echo "A média entre <span class='num'>". number_format($n1, 1). "</span> ";
    echo "e <span class='num'>". number_format($n2, 1). "</span> "; 
    echo "é igual a <span class='num'>". number_format($media, 1). "</span>";
    echo "<br>Situação do aluno: <span class='num'>$sit</span>";
?>

<style>
    .num {
        color: red;
    }
</style>
