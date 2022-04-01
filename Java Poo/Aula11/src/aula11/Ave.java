package aula11;

public class Ave extends Animal {
    // Atributos
    private String corPena;

    // Método construtor
    protected Ave(float p, int i, int m, String c) {
        super(p, i, m);
        this.setCorPena(c);
    }

    // Métodos
    public void fazerNinho() {
        System.out.println("Construiu um ninho");
    }

    @Override
    public void locomover() {
        System.out.println("Voando");
    }
    @Override
    public void alimentar() {
        System.out.println("Se alimentando");
    }
    @Override
    public void emitirSom() {
        System.out.println("Som de ave");
    }

    // Métodos especiais
    public void setCorPena(String c) {
        this.corPena = c;
    }
    public String getCorPena() {
        return this.corPena;
    }
}
