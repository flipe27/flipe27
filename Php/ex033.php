<?php 
    # Funções String
    # printf()
    $prod = 'leite';
    $preco = 4.5;
    printf("O %s custa R$%.2f<br>", $prod, $preco);

    # print_r()
    $x[0] = 3;
    $x[1] = 4;
    $x[2] = 5;
    print_r($x);  # Existe também as opções de 'var_dump()' e 'var_export()'

    $v2 = array(3, 4, 5, 6, 7);
    print("<br>");
    print_r($v2);

    # wordwrap()
    $txt = 'Este é um exemplo de um texto gigante que...';
    $res = wordwrap($txt, 5, "<br>", false);  # Com o 'true' caso a palavra tenha mais do que 5 letras a palavra é quebrada
    print("<br>");
    echo $res;

    # strlen()
    $st = "Curso em Video"; 
    $r = strlen($st);  # A função conta acentos como caracteres a mais
    print("<br>");
    echo $r;

    # trim()
    $nome = '   José da Silva   ';
    print("<br>");
    echo trim($nome);  # Existem também as opções 'rtrim()' e 'ltrim()' que retiram os espaços na direita ou esquerda

    # str_word_count()
    $frase = 'Eu estou estudando PHP agora';
    print("<br>");
    print(str_word_count($frase, 0));  # O parâmetro '0' conta a quantidade de palavras, já o '1' gera um array delas

    # explode()
    $site = 'Curso em Video';
    print("<br>");
    print_r(explode(' ', $site));

    # str_split()
    $name = 'Maria';
    print("<br>");
    print_r(str_split($name));

    # implode()
    $vetor[0] = 'Curso';
    $vetor[1] = 'em';
    $vetor[2] = 'Video';
    print("<br>");
    print(implode('#', $vetor));  # A função 'join()' possui o mesmo comportamento

    # chr()
    $letra = chr(67);
    print("<br>");
    echo "A letra de código 67 é $letra<br>";

    # ord()
    $letter = ord('C');
    echo "O código da letra C é $letter";
?>
