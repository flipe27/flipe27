<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notas de um aluno</title>
</head>
<body>
    <?php 
        $nota1 = $_GET['n1'];
        $nota2 = $_GET['n2'];
        $media = ($nota1 + $nota2) / 2;
        echo "A média entre $nota1 e $nota2 é $media";
        echo "</br>A situação do aluno é: ". (($media >= 6) ? 'Aprovado!' : 'Reprovado!');
    ?>
</body>
</html>