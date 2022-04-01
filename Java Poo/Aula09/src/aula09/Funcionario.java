package aula09;

public class Funcionario extends Pessoa {  // Classe filha/sub classe da classe "Pessoa"
    // Atributos
    private String setor;
    private boolean trabalhando;

    // Método construtor
    public Funcionario(String n, int i, String s, String se, boolean t) {
        super(n, i, s);
        this.setSetor(se);
        this.setTrabalhando(t);
    }

    // Métodos
    public void mudarTrabalho() {
        this.setTrabalhando(!this.isTrabalhando());
    }

    // Métodos especiais
    public void setSetor(String s) {
        this.setor = s;
    }
    public String getSetor() {
        return this.setor;
    }
    public void setTrabalhando(boolean t) {
        this.trabalhando = t;
    }
    public boolean isTrabalhando() {
        return this.trabalhando;
    }
}
