// Press "F8" to run
// Formatações de números
var n1 = 1548.5
console.log(n1.toFixed(2))  // "toFixed(n)" define a quantidade de casas decimais
console.log(n1.toFixed(2).replace('.', ','))  // "replace" troca o primeiro parâmetro pelo segundo
console.log(n1.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'}))  // Formatação do real brasileiro
