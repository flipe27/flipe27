package aula11;

public abstract class Animal {
    // Atributos
    protected float peso;
    protected int idade, membros;

    // Método construtor
    protected Animal(float p, int i, int m) {
        this.setPeso(p);
        this.setIdade(i);
        this.setMembros(m);
    }

    // Métodos
    public abstract void locomover();
    public abstract void alimentar();
    public abstract void emitirSom();

    // Métodos especiais
    protected void setPeso(float p) {
        this.peso = p;
    }
    protected float getPeso() {
        return this.peso;
    }
    protected void setIdade(int i) {
        this.idade = i;
    }
    protected int getIdade() {
        return this.idade;
    }
    protected void setMembros(int m) {
        this.membros = m;
    }
    protected int getMembros() {
        return this.membros;
    }
}
