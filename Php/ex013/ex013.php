<?php 
    $txt = isset($_GET['txt']) ? $_GET['txt'] : 'Texto Genérico';
    $tam = isset($_GET['tam']) ? $_GET['tam'] : '12pt';
    $cor = isset($_GET['cor']) ? $_GET['cor'] : '#000000';

    echo "<p id='texto'>$txt</p>";
?>

<style>
    #texto {
        font-size: <?php echo $tam; ?>;
        color: <?php echo $cor; ?>;
    }
</style>