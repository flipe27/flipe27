package aula11;

public class Orca extends Mamifero {
    // Métodos
    protected Orca(float p, int i, int m, String c) {
        super(p, i, m, c);
    }

    @Override
    public void locomover() {
        System.out.println("Nadando");
    }
}
