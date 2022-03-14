<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funções Aritméticas</title>
</head>
<body>
    <?php
        $v1 = $_GET['x'];
        $v2 = $_GET['y'];

        echo "<h2>Valores recebidos: $v1 e $v2</h2>";

        echo "O valor absoluto de $v2 é ". abs($v2);
        echo "</br>O valor de $v2<sup>$v1</sup> é ". pow($v2, $v1);
        echo "</br>A raíz de $v1 é ". sqrt($v1);
        echo "</br>A valor arredondado de $v2 é ". round($v2);  // 'ceil()' e 'floor()' também arredondam
        echo "</br>A parte interia de $v2 é ". intval($v2);
        echo "</br>O valor de $v1 em moeda é R$". number_format($v1, 2, ",", ".");
    ?>
</body>
</html>