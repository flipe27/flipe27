package aula12;

public abstract class Mamifero {
    // Atributos
    protected float peso;
    protected int idade, membros;
    protected String corPelo;

    // Método construtor
    public Mamifero(float peso, int idade, int membros, String corPelo) {
        this.setPeso(peso);
        this.setIdade(idade);
        this.setMembros(membros);
        this.setCorPelo(corPelo);
    }

    // Métodos
    public void emitirSom() {
        System.out.println("Som de mamífero");
    }

    // Métodos especiais
    public void setPeso(float p) {
        this.peso = p;
    }
    public float getPeso() {
        return this.peso;
    }
    public void setIdade(int i) {
        this.idade = i;
    }
    public int getIdade() {
        return this.idade;
    }
    public void setMembros(int m) {
        this.membros = m;
    }
    public int getMembros() {
        return this.membros;
    }
    public void setCorPelo(String cp) {
        this.corPelo = cp;
    }
    public String  getCorPelo() {
        return this.corPelo;
    }
}
