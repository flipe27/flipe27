package aula09;

public class Pessoa {  // Classe mãe/progenitora/super classe
    // Atributos
    private String nome;
    private int idade;
    private String sexo;

    // Método construtor
    public Pessoa(String n, int i, String s) {
        this.setNome(n);
        this.setIdade(i);
        this.setSexo(s);
    }

    // Métodos
    public void fazerAniv() {
        this.setIdade(this.getIdade() + 1);
    }
    public String toString() {
        return "Pessoa {\nnome = " + this.getNome() + ",\nidade = " + this.getIdade() +
                ",\nsexo = " + this.getSexo() + "\n}";
    }

    // Métodos especiais
    public void setNome(String n) {
        this.nome = n;
    }
    public String getNome() {
        return this.nome;
    }
    public void setIdade(int i) {
        this.idade = i;
    }
    public int getIdade() {
        return this.idade;
    }
    public void setSexo(String s) {
        this.sexo = s;
    }
    public String getSexo() {
        return this.sexo;
    }
}
