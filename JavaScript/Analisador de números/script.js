let res = window.document.getElementById('res')
let valores = []
let maior = 0
let menor = 0
let soma = 0

function checarNum(num) {
    if (num < 1 || num > 100) {
        return true
    } else if (valores.indexOf(num) != -1) {
        return true
    } else {
        return false
    }
}

function adicionar() {
    let num = Number(window.document.getElementById('num').value)
    let adicionados = window.document.getElementById('adicionados')
    res.innerHTML = ''

    if (checarNum(num)) {
        window.alert('Valor inválido ou já encontrado na lista!')
    } else {
        if (valores.length == 0) {
            maior = num
            menor = num
        } else if (num > maior) {
            maior = num
        } else {
            menor = num
        }

        valores.push(num)
        soma += num
        adicionados.innerHTML += `<option>Valor ${num} adicionado</option>`
    }
}

function finalizar() {
    if (valores.length == 0) {
        window.alert('Adicione valores antes de finalizar!')
    } else {
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${valores.length} números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
        res.innerHTML += `<p>Somando todos os valores, temos ${soma}.</p>`
        res.innerHTML += `<p>A média dos valores digitados é ${soma / valores.length}.</p>`
    }
}
