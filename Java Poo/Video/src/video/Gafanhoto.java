package video;

public class Gafanhoto extends Pessoa {
    // Atributos
    private String login;
    private int totAssistido;

    // Método construtor
    public Gafanhoto(String nome, String sexo, int idade, String login) {
        super(nome, sexo, idade);
        this.setLogin(login);
        this.setTotAssistido(0);
    }

    // Métodos
    public void viuMaisUm() {
        this.setTotAssistido(this.getTotAssistido() + 1);
    }
    @Override
    public String toString() {
        return "Gafanhoto {\n" + super.toString() + ",\nlogin = " + this.getLogin() + "\ntotAssistido = " +
                this.getTotAssistido() + "}";
    }

    // Métodos especiais
    private void setLogin(String l) {
        this.login = l;
    }
    private String getLogin() {
        return this.login;
    }
    public void setTotAssistido(int ta) {
        this.totAssistido = ta;
    }
    public int getTotAssistido() {
        return this.totAssistido;
    }
}
