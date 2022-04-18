function contar() {
    var inicio = window.document.getElementById('inicio')
    var fim = window.document.getElementById('fim')
    var passo = window.document.getElementById('passo')
    var res = window.document.getElementById('res')

    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
        res.innerHTML = 'Impossível contar!'
    } else {
        var i = Number(inicio.value)
        var f = Number(fim.value)
        var p = Number(passo.value)
        res.innerHTML = '<p>Contando: </p>'

        if (p == 0) {
            window.alert('Passo inválido! Considerando passo como 1.')
            p = 1
        }
        if (i < f) {
            for (i; i <= f; i += p) {
                res.innerHTML += `${i} &#x1F449 `
            }
        } else {
            for (i; i >= f; i -= p) {
                res.innerHTML += `${i} &#x1F449 `
            }
        }
        res.innerHTML += '&#x1F3C1'
    }
}
