package video;

public abstract class Pessoa {
    // Atributos
    protected String nome, sexo;
    protected int idade, experiencia;

    // Método construtor
    protected Pessoa(String nome, String sexo, int idade) {
        this.setNome(nome);
        this.setSexo(sexo);
        this.setIdade(idade);
        this.setExperiencia(0);
    }

    // Métodos
    protected void ganharExp() {
        this.setExperiencia(this.getExperiencia() + 1);
    }
    @Override
    public String toString() {
        return "Pessoa {nome = " + this.getNome() + ",\nsexo = " + this.getSexo() + ",\nidade = " + this.getIdade() +
                ",\nexperiencia = " + this.getExperiencia() + "}";
    }

    // Métodos especiais
    protected void setNome(String n) {
        this.nome = n;
    }
    protected String getNome() {
        return this.nome;
    }
    protected void setSexo(String s) {
        this.sexo = s;
    }
    protected String getSexo() {
        return this.sexo;
    }
    protected void setIdade(int i) {
        this.idade = i;
    }
    protected int getIdade() {
        return this.idade;
    }
    protected void setExperiencia(int e) {
        this.experiencia = e;
    }
    protected int getExperiencia() {
        return this.experiencia;
    }
}
