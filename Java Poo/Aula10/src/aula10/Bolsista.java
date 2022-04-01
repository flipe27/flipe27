package aula10;

public class Bolsista extends Aluno {
    // Atributos
    private float bolsa;

    // Método construtor
    public Bolsista(String n, int i, String s, int m, String c, float b) {
        super(n, i, s, m, c);
        this.setBolsa(b);
    }

    // Métodos
    public void renovarBolsa() {
        System.out.println("Renovando bolsa de " + this.getNome());
    }
    @Override
    public void pagarMensalidade() {
        System.out.println(this.getNome() + " é bolsista! Pagamento facilitado.");
    }

    // Métodos especiais
    public void setBolsa(float b) {
        this.bolsa = b;
    }
    public float getBolsa() {
        return this.bolsa;
    }
}
