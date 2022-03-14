<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Referência</title>
</head>
<body>
    <?php
        $a = 3;
        $b = $a;
        $b += 5;
        echo "O valor de a é $a e o valor de b é $b";

        $site = 'cursoemvideo';
        $$site = 'cursophp';
        echo "</br>O site 1 é $site e o site 2 é $cursoemvideo";
    ?>
</body>
</html> 