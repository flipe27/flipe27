package aula12;

public class Aula12 {
    public static void main(String[] args) {
        // Programa principal
        Cachorro c = new Cachorro(30f, 12, 4, "Azul");

        c.emitirSom();
        c.reagir("Cheguei");
        c.reagir("Meu bacano");
        c.reagir(11);
        c.reagir(21);
        c.reagir(true);
        c.reagir(2, 12.5f);
    }
}
