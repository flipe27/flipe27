<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="get" action="ex024.php">
        Número: 
        <select name="num">
            <?php 
                $cont = 1;
                while($cont <= 10) {
                    echo "<option value='$cont'>$cont</option>";
                    $cont++;
                }
            ?>
        </select>
        <input type="submit" value="Tabuada">
    </form>
</body>
</html>