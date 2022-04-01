package aula07;

public class Lutador implements Luta {
    // Atributos
    private String nome, nacionalidade, categoria;
    private float altura, peso;
    private int idade, vitorias, derrotas, empates;

    // Métodos
    public Lutador(String no, String na, int id, float al, float pe, int vi, int de, int em) {
        this.setNome(no);
        this.setNacionalidade(na);
        this.setIdade(id);
        this.setAltura(al);
        this.setPeso(pe);
        this.setVitorias(vi);
        this.setDerrotas(de);
        this.setEmpates(em);
    }

    private void setNome(String n) {
        this.nome = n;
    }
    public String getNome() {
        return this.nome;
    }
    private void setNacionalidade(String n) {
        this.nacionalidade = n;
    }
    private String getNacionalidade() {
        return this.nacionalidade;
    }
    private void setIdade(int i) {
        this.idade = i;
    }
    private int getIdade() {
        return this.idade;
    }
    private void setAltura(float a) {
        this.altura = a;
    }
    private float getAltura() {
        return this.altura;
    }
    private void setPeso(float p) {
        this.peso = p;
        this.setCategoria();
    }
    private float getPeso() {
        return this.peso;
    }
    private void setCategoria() {
        if (this.peso < 52.2f) {
            this.categoria = "Inválido";
        } else if (this.peso <= 70.3f) {
            this.categoria = "Leve";
        } else if (this.peso <= 83.9f) {
            this.categoria = "Médio";
        } else if (this.peso <= 120.2f) {
            this.categoria = "Pesado";
        } else {
            this.categoria = "Inválido";
        }
    }
    public String getCategoria() {
        return this.categoria;
    }
    private void setVitorias(int v) {
        this.vitorias = v;
    }
    private int getVitorias() {
        return this.vitorias;
    }
    private void setDerrotas(int d) {
        this.derrotas = d;
    }
    private int getDerrotas() {
        return this.derrotas;
    }
    private void setEmpates(int e) {
        this.empates = e;
    }
    private int getEmpates() {
        return this.empates;
    }

    @Override
    public void apresentar() {
        System.out.println("Chegou a hora! Apresentamos o lutador " + this.getNome());
        System.out.println("Diretamente de " + this.getNacionalidade());
        System.out.printf("Com %d anos e %.2fm de altura", this.getIdade(), this.getAltura());
        System.out.println("\nPesando " + this.getPeso() + "kg");
        System.out.print(this.getVitorias() + " vitórias, ");
        System.out.print(this.getDerrotas() + " derrotas e ");
        System.out.println(this.getEmpates() + " empates");
    }
    @Override
    public void status() {
        System.out.println(this.getNome());
        System.out.println("É um peso " + this.getCategoria());
        System.out.println(this.getVitorias() + " vitórias");
        System.out.println(this.getDerrotas() + " derrotas");
        System.out.println(this.getEmpates() + " empates");
    }
    @Override
    public void ganharLuta() {
        this.setVitorias(this.getVitorias() + 1);
    }
    @Override
    public void perderLuta() {
        this.setDerrotas(this.getDerrotas() + 1);
    }
    @Override
    public void empatarLuta() {
        this.setEmpates(this.getEmpates() + 1);
    }
}
