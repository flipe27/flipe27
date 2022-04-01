package aula11;

public class Mamifero extends Animal {
    // Atributos
    private String corPelo;

    // Método construtor
    protected Mamifero(float p, int i, int m, String c) {
        super(p, i, m);
        this.setCorPelo(c);
    }

    // Métodos
    @Override
    public void locomover() {
        System.out.println("Correndo");
    }
    @Override
    public void alimentar() {
        System.out.println("Se alimentando");
    }
    @Override
    public void emitirSom() {
        System.out.println("Som de mamífero");
    }

    // Métodos especiais
    public void setCorPelo(String c) {
        this.corPelo = c;
    }
    public String getCorPelo() {
        return this.corPelo;
    }
}
