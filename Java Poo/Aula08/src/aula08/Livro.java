package aula08;

public class Livro implements Publicacao {
    // Atributos
    private String titulo, autor;
    private int totPaginas, pagAtual;
    private boolean aberto;
    private Pessoa leitor;

    // Métodos
    public Livro(String t, String a, int tp, Pessoa l) {
        this.setTitulo(t);
        this.setAutor(a);
        this.setTotPaginas(tp);
        this.setPagAtual(0);
        this.setAberto(false);
        this.setLeitor(l);
    }

    private void setTitulo(String t) {
        this.titulo = t;
    }
    private String getTitulo() {
        return this.titulo;
    }
    private void setAutor(String at) {
        this.autor = at;
    }
    private String getAutor() {
        return this.autor;
    }
    private void setTotPaginas(int tp) {
        this.totPaginas = tp;
    }
    private int getTotPaginas() {
        return this.totPaginas;
    }
    private void setPagAtual(int pa) {
        this.pagAtual = pa;
    }
    public int getPagAtual() {
        return this.pagAtual;
    }
    private void setAberto(boolean a) {
        this.aberto = a;
    }
    private boolean getAberto() {
        return this.aberto;
    }
    private void setLeitor(Pessoa l) {
        this.leitor = l;
    }
    private Pessoa getLeitor() {
        return this.leitor;
    }

    public String detalhes() {
        return "Livro {título = " + this.getTitulo() + ", autor = " + this.getAutor() + ", totPaginas = "
                + this.getTotPaginas() + ", pagAtual = " + this.getPagAtual() + ",\naberto = " + this.getAberto()
                + ", leitor = " + this.getLeitor().getNome() + ", idadeLeitor = " + this.getLeitor().getIdade()
                + ", sexoLeitor = " + this.getLeitor().getSexo() + "}";
    }

    @Override
    public void abrir() {
        this.setAberto(true);
    }
    @Override
    public void fechar() {
        this.setAberto(false);
    }
    @Override
    public void folhear(int p) {
        if (p > this.getTotPaginas()) {
            this.setPagAtual(0);
        } else {
            this.setPagAtual(p);
        }
    }
    @Override
    public void avancarPag() {
        this.setPagAtual(this.getPagAtual() + 1);
    }
    @Override
    public void voltaPag() {
        this.setPagAtual(this.getPagAtual() - 1);
    }
}
