<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores relacionais</title>
</head>
<body>
    <?php
        $num1 = $_GET['n1'];
        $num2 = $_GET['n2'];
        $tipo = $_GET['op'];
        echo "Os valores passados foram $num1 e $num2";
        $r = ($tipo == 's') ? $num1 + $num2 : $num1 * $num2;
        echo "</br>O resultado é $r";

        $a = 3;
        $b = '3';
        $c = ($a === $b) ? 'Sim' : 'Não';
        echo "</br>As variáveis a e b são idênticas? $c";
    ?>
</body>
</html>