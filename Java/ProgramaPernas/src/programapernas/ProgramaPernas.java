package programapernas;

import java.util.Scanner;

public class ProgramaPernas {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite a quantidade de pernas: ");
        int pernas = teclado.nextInt();
        String tipo;

        switch(pernas) {
            case 1:
                tipo = "Saci";
                break;
            case 2:
                tipo = "Bípede";
                break;
            case 4:
                tipo = "Quadrúpede";
                break;
            case 6, 8:
                tipo = "Aranha";
                break;
            default:
                tipo = "E.T.";
        }
        System.out.println("Pela quantidade de pernas o tipo é " + tipo);
    }
}
