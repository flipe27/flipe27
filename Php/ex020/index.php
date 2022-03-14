<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="get" action="ex020.php">
        <?php 
            $cont = 1;
            while($cont <= 5) {
                echo "Valor " . $cont . ": <input type='number' name='v" . $cont . "' min='0' max='100'><br>";
                $cont++;
            }
        ?>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>