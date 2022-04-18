function tabuada(){
    var num = window.document.getElementById('num')
    var tabuada = window.document.getElementById('tabuada')

    if (num.value.length == 0) {
        window.alert('Por favor, digite um número!')
    } else {
        var n = Number(num.value)
        tabuada.innerHTML = ''

        for (var cont = 1; cont <= 10; cont++) {
            var item = document.createElement('option')
            item.text = `${n} x ${cont} = ${n * cont}`
            tabuada.appendChild(item)
        }
    }
}
