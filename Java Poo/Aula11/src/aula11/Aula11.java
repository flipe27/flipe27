package aula11;

public class Aula11 {
    public static void main(String[] args) {
        // Programa principal
        Mamifero m = new Mamifero(20f, 14, 4, "Branco");
        Peixe p = new Peixe(544f, 20, 3, "Cinza");
        Ave a = new Ave(0.280f, 66, 2, "Azul");
        Orca o = new Orca(3000f, 30, 3, "Preto");

        m.locomover();
        p.soltarBolha();
        a.emitirSom();
        o.locomover();
    }
}
