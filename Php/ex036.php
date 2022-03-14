<pre>
<?php 
    $cadastro = array( 'nome' => 'Ana',
                    'idade' => 23,
                    'peso' => 65.5);
    $cadastro['fuma'] = true;
    print_r($cadastro);
    foreach($cadastro as $campo => $valor) {
        print("O valor de $campo é $valor<br>");
    }
?>
</pre>
