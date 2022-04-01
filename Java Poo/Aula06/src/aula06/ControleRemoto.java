package aula06;

public class ControleRemoto implements Controlador {
    // Atributos
    private int volume;
    private boolean ligado;
    private boolean tocando;

    // Métodos especiais
    public ControleRemoto() {  // Método construtor
        this.setVolume(50);
        this.setLigado(false);
        this.setTocando(false);
    }

    private void setVolume(int v) {
        this.volume = v;
    }
    private int getVolume() {
        return this.volume;
    }
    private void setLigado(boolean l) {
        this.ligado = l;
    }
    private boolean getLigado() {
        return this.ligado;
    }
    private void setTocando(boolean t) {
        this.tocando = t;
    }
    private boolean getTocando() {
        return this.tocando;
    }

    // Métodos abstratos
    @Override
    public void ligar() {
        this.setLigado(true);
    }
    @Override
    public void desligar() {
        this.setLigado(false);
    }
    @Override
    public void abrirMenu() {
        System.out.println("------ MENU ------");
        System.out.println("Está ligado? " + this.getLigado());
        System.out.print("Volume: " + this.getVolume());

        for (int i = 0; i <= getVolume(); i += 10) {
            System.out.print("|");
        }

        System.out.println("\nEstá tocando? " + this.getTocando());
    }
    @Override
    public void fecharMenu() {
        System.out.println("Fechando menu...");
    }
    @Override
    public void maisVolume() {
        if (this.getLigado()) {
            this.setVolume(this.getVolume() + 10);
        }
    }
    @Override
    public void menosVolume() {
        if (this.getLigado()) {
            this.setVolume(this.getVolume() - 10);
        }
    }
    @Override
    public void ligarMudo() {
        if (this.getLigado() && this.getVolume() > 0) {
            this.setVolume(0);
        }
    }
    @Override
    public void desligarMudo() {
        if (this.getLigado() && this.getVolume() == 0) {
            this.setVolume(50);
        }
    }
    @Override
    public void play() {
        if (this.getLigado() && !this.getTocando()) {
            this.setTocando(true);
        }
    }
    @Override
    public void pause() {
        if (this.getLigado() && this.getTocando()) {
            this.setTocando(false);
        }
    }
}
