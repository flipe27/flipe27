<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="get" action="ex026.php">
        Número: 
        <select name="num">
            <?php 
                for($cont = 1; $cont <= 10; $cont++) {
                    echo "<option value='$cont'>$cont</option>";
                }
            ?>
        </select>
        <input type="submit" value="Tabuada">
    </form>
</body>
</html>