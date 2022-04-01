package aula07;

import java.util.Random;

public class Lutar {
    // Atributos
    private Lutador desafiado, desafiante;
    private boolean aprovada;

    // Métodos
    public void setDesafiado(Lutador dd) {
        this.desafiado = dd;
    }
    public Lutador getDesafiado() {
        return this.desafiado;
    }
    public void setDesafiante(Lutador dt) {
        this.desafiante = dt;
    }
    public Lutador getDesafiante() {
        return this.desafiante;
    }
    public void setAprovada(boolean a) {
        this.aprovada = a;
    }
    public boolean getAprovada() {
        return this.aprovada;
    }

    public void marcarLuta(Lutador l1, Lutador l2) {
        if (l1.getCategoria().equals(l2.getCategoria()) && l1 != l2) {
            this.setAprovada(true);
            this.setDesafiado(l1);
            this.setDesafiante(l2);
        } else {
            this.setAprovada(false);
            this.setDesafiado(null);
            this.setDesafiante(null);
        }
    }
    public void lutar() {
        if (this.getAprovada()) {
            System.out.println("------------ DESAFIADO ------------");
            this.getDesafiado().apresentar();
            System.out.println("----------- DESAFIANTE -----------");
            this.getDesafiante().apresentar();

            Random aleatorio = new Random();
            int vencedor = aleatorio.nextInt(3);

            switch (vencedor) {
                case 0 -> {  // Empate
                    System.out.println("---------------------");
                    System.out.println("Empatou");
                    this.desafiado.empatarLuta();
                    this.desafiante.empatarLuta();
                }
                case 1 -> {  // Desafiado vence
                    System.out.println("---------------------");
                    System.out.println(this.desafiado.getNome() + " venceu!");
                    this.desafiado.ganharLuta();
                    this.desafiante.perderLuta();
                }
                case 2 -> {  // Desafiante venceu
                    System.out.println("---------------------");
                    System.out.println(this.desafiante.getNome() + " venceu");
                    this.desafiado.perderLuta();
                    this.desafiante.ganharLuta();
                }
            }
            System.out.println("---------------------");
            this.desafiado.status();
            System.out.println("---------------------");
            this.desafiante.status();
        } else {
            System.out.println("A luta não pode acontecer!");
        }
    }
}
