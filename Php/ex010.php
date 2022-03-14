<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Idades de voto</title>
</head>
<body>
    <?php 
        $ano = $_GET['an'];
        $idade = 2022 - $ano;
        echo "Idade = $idade. Voto ". (($idade >= 18 and $idade < 65) ? 'obrigatório' : 'não obrigatório');
    ?>
</body>
</html>