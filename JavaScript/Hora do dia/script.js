var agora = new Date()
var hora = agora.getHours()
var horaAtual = window.document.getElementById('horaAtual')
var corpo = window.document.getElementById('corpo')
var img = window.document.getElementById('img')

horaAtual.innerText += ` ${hora} horas.`

if (hora >= 6 && hora < 12) {
    corpo.style.backgroundColor = 'rgb(120, 120, 190)'
    img.src = 'dia.jpg'
} else if (hora >= 12 && hora < 18) {
    corpo.style.backgroundColor = 'rgb(167, 167, 91)'
    img.src = 'tarde.webp'
} else {
    corpo.style.backgroundColor = 'rgb(56, 54, 54)'
    img.src = 'noite.webp'
}
