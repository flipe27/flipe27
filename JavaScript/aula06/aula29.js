// Press "F8" to run
// Modelo de orientação a objeto
let amigo = {nome:'José', 
            sexo:'M', 
            peso:85.4, 
            engordar(p) {
                console.log('Engordou')
                this.peso += p
            }}
console.log(amigo)
amigo.engordar(2)
console.log(`${amigo.nome} pesa ${amigo.peso}`)
