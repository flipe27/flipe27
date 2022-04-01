package video;

public class Visualizacao {
    // Atributos
    private Gafanhoto espectador;
    private Video filme;

    // Método construtor
    public Visualizacao(Gafanhoto espectador, Video filme) {
        this.setEspectador(espectador);
        this.setFilme(filme);
        this.getEspectador().viuMaisUm();
        this.getFilme().setViews(this.getFilme().getViews() + 1);
    }

    // Métodos
    @Override
    public String toString() {
        return "Visualizacao {espectador = " + this.getEspectador().getNome() +
                ",\nfilme = " + this.getFilme().getTitulo() + "}";
    }
    public void avaliar() {
        this.getFilme().setAvaliacao(5);
    }
    public void avaliar(int nota) {
        this.getFilme().setAvaliacao(nota);
    }

    // Métodos especiais
    private void setEspectador(Gafanhoto e) {
        this.espectador = e;
    }
    private Gafanhoto getEspectador() {
        return this.espectador;
    }
    private void setFilme(Video f) {
        this.filme = f;
    }
    private Video getFilme() {
        return this.filme;
    }
}
