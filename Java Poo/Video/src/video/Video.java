package video;

public class Video implements AcoesVideo {
    // Atributos
    private String titulo;
    private int avaliacao, views, curtidas;
    private boolean reproduzindo;

    // Método construtor
    public Video(String titulo) {
        this.setTitulo(titulo);
        this.setViews(0);
        this.setCurtidas(0);
        this.setReproduzindo(false);
    }

    // Métodos
    @Override
    public String toString() {
        return "Video {titulo = " + this.getTitulo() + ",\navaliacao = " + this.getAvaliacao() +
                ",\nviews = " + this.getViews() + ",\ncurtidas = " + this.getCurtidas() +
                ",\nreproduzindo = " + this.isReproduzindo() + "}";
    }
    @Override
    public void play() {
        this.setReproduzindo(true);
    }
    @Override
    public void pause() {
        this.setReproduzindo(false);
    }
    @Override
    public void like() {
        this.setCurtidas(this.getCurtidas() + 1);
    }

    // Métodos especiais
    private void setTitulo(String t) {
        this.titulo = t;
    }
    public String getTitulo() {
        return this.titulo;
    }
    public void setAvaliacao(int a) {
        this.avaliacao = this.getAvaliacao() + a;
    }
    public int getAvaliacao() {
        return this.avaliacao;
    }
    public void setViews(int v) {
        this.views = v;
    }
    public int getViews() {
        return this.views;
    }
    private void setCurtidas(int c) {
        this.curtidas = c;
    }
    private int getCurtidas() {
        return this.curtidas;
    }
    private void setReproduzindo(boolean r) {
        this.reproduzindo = r;
    }
    private boolean isReproduzindo() {
        return this.reproduzindo;
    }
}
