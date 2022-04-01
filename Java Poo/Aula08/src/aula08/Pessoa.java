package aula08;

public class Pessoa {
    // Atributos
    private String nome, sexo;
    private int idade;

    // Métodos
    public Pessoa(String no, int id, String sx) {
        this.setNome(no);
        this.setIdade(id);
        this.setSexo(sx);
    }

    private void setNome(String n) {
        this.nome = n;
    }
    public String getNome() {
        return this.nome;
    }
    private void setIdade(int i) {
        this.idade = i;
    }
    public int getIdade() {
        return this.idade;
    }
    private void setSexo(String s) {
        this.sexo = s;
    }
    public String getSexo() {
        return this.sexo;
    }

    public void fazerAniver() {
        this.setIdade(this.getIdade() + 1);
    }
}
