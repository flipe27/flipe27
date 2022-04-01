package aula11;

public class Peixe extends Animal {
    // Atributos
    private String corEscama;

    // Método construtor
    protected Peixe(float p, int i, int m, String c) {
        super(p, i, m);
        this.setCorEscama(c);
    }

    // Métodos
    public void soltarBolha() {
        System.out.println("Soltou uma bolha");
    }

    @Override
    public void locomover() {
        System.out.println("Nadando");
    }
    @Override
    public void alimentar() {
        System.out.println("Se alimentando");
    }
    @Override
    public void emitirSom() {
        System.out.println("Peixe não faz som");
    }

    // Métodos especiais
    public void setCorEscama(String c) {
        this.corEscama = c;
    }
    public String getCorEscama() {
        return this.corEscama;
    }
}
