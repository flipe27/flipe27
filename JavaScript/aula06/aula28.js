// Press "F8" to run
function fatorial(num) {  // Função recursiva, ou seja, ela pode chamar ela mesma
    if (num == 1) {
        return num
    } else {
        return num * fatorial(num - 1)
    }
}

console.log(fatorial(5))
