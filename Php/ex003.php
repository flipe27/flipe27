<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operações aritméticas</title>
</head>
<body>
    <?php
        $n1 = $_GET['a'];
        $n2 = $_GET['b'];
        $media = ($n1 + $n2) / 2;

        echo "n1 = $n1, n2 = $n2";

        echo "</br>A soma vale ". ($n1 + $n2);
        echo "</br>A subtração vale ". ($n1 - $n2);
        echo "</br>A multiplicação vale ". ($n1 * $n2);
        echo "</br>A divisão vale ". ($n1 / $n2);
        echo "</br>O resto vale ". ($n1 % $n2);
        echo "</br>A méida vale $media";
    ?>
</body>
</html>