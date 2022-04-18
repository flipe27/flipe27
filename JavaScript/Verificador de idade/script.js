function verificar() {
    var agora = new Date()
    var anoAtual = agora.getFullYear()
    var anoNasc = Number(window.document.getElementById('ano').value)
    var sexo = window.document.getElementsByName('sexo')
    var res = window.document.getElementById('res')
    var img = document.createElement('img')

    img.setAttribute('id', 'img')

    if (anoNasc <= 0 || anoNasc > anoAtual) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var idade = anoAtual - anoNasc
        if (sexo[0].checked) {
            res.innerHTML = `Detectamos Homem com ${idade} anos`
            if (idade < 10) {
                img.setAttribute('src', 'imagens/foto-bebe-m.png')
            } else if (idade < 25) {
                img.setAttribute('src', 'imagens/foto-jovem-m.png')
            } else if (idade < 60) {
                img.setAttribute('src', 'imagens/foto-adulto-m.png')
            } else {
                img.setAttribute('src', 'imagens/foto-idoso-m.png')
            }
        } else {
            res.innerHTML = `Detectamos Mulher com ${idade} anos`
            if (idade < 10) {
                img.setAttribute('src', 'imagens/foto-bebe-f.png')
            } else if (idade < 25) {
                img.setAttribute('src', 'imagens/foto-jovem-f.png')
            } else if (idade < 60) {
                img.setAttribute('src', 'imagens/foto-adulto-f.png')
            } else {
                img.setAttribute('src', 'imagens/foto-idoso-f.png')
            }
        }
        res.style.textAlign = 'center'
        res.appendChild(img)
    }
}
