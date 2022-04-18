// Press "F8" to run
function parimpar(num) {  // Função que possui parâmetro, ação e resultado
    if (num % 2 == 0) {
        return 'Par!'
    } else {
        return 'Ímpar!'
    }
}

let res = parimpar(11)  // Chamada para a função "parimpar()"
console.log(res)
