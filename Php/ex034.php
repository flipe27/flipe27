<?php 
    # strtolower()
    $min = 'PaulO FelLipe';
    print("Seu nome em minuscúlas é " . strtolower($min) . "<br>");

    # strtoupper()
    $mai = 'paulo fellipe';
    print("Seu nome em maiúsculas é " . strtoupper($mai) . "<br>");

    # ucfirst()
    $nome = 'paulo fellipe';
    print("Seu nome é " . ucfirst($nome));

    # ucwords()
    $palavras = 'paulo fellipe';
    print("<br>Seu nome é " . ucwords($palavras));

    # strrev()
    $contrario = 'paulo fellipe';
    print("<br>" . strrev($contrario));

    # strpos()
    $frase = 'Estou aprendendo PHP';
    print("<br>A string foi encontrada na posição " . strpos($frase, 'PHP'));

    # stripos()
    $fmin = 'Estou aprendendo PHP';
    print("<br>A string foi encontrada na posição " . stripos($frase, 'php'));

    # substr_count()
    $cont = 'Estou aprendendo PHP no Curso em Vídeo de PHP';
    print("<br>PHP encontrado " . substr_count($cont, 'PHP') . " vezes");

    # substr()
    $site = 'Curso em Video';
    print("<br>" . substr($site, 0, 5));
    print("<br>" . substr($site, -5));

    # str_pad()
    $tamanho = 'Guanabara';
    print("<br>" . str_pad($tamanho, 30, ' ', STR_PAD_RIGHT));

    # str_repeat()
    print("<br>O texto gerado foi " . str_repeat('PHP', 5));

    # str_replace()
    $mat = 'Gosto de estudar Matemática';
    print("<br>" . str_replace('Matemática', 'Programação', $mat))  # Existe também a opção de 'str_ireplace()'
?>
