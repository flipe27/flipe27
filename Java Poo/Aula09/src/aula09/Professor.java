package aula09;

public class Professor extends Pessoa {  // Classe filha/sub classe da classe "Pessoa"
    // Atributos
    private String especialidade;
    private float salario;

    // Método construtor
    public Professor(String n, int i, String s, String e, float sa) {
        super(n, i, s);
        this.setEspecialidade(e);
        this.setSalario(sa);
    }

    // Métodos
    public void receberAum(float a) {
        this.setSalario(this.getSalario() + a);
    }

    // Métodos especiais
    public void setEspecialidade(String e) {
        this.especialidade = e;
    }
    public String getEspecialidade() {
        return this.especialidade;
    }
    public void setSalario(float s) {
        this.salario = s;
    }
    public float getSalario() {
        return this.salario;
    }
}
