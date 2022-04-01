package aula10;

public class Aluno extends Pessoa {
    // Atributos
    private int matricula;
    private String curso;

    // Método construtor
    public Aluno(String n, int i, String s, int m, String c) {
        super(n, i, s);
        this.setMatricula(m);
        this.setCurso(c);
    }

    // Métodos
    public void pagarMensalidade() {
        System.out.println("Pagando mensalidade do aluno " + this.getNome());
    }

    // Métodos especiais
    public void setMatricula(int m) {
        this.matricula = m;
    }
    public int getMatricula() {
        return this.matricula;
    }
    public void setCurso(String c) {
        this.curso = c;
    }
    public String getCurso() {
        return this.curso;
    }
}
