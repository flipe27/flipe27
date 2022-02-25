package vetor01;

import java.util.Arrays;

public class Vetor01 {
    public static void main(String[] args) {
        int[] n = {3, 2, 8, 7, 5, 4};

        for(int cont = 0; cont < 6; cont++) {
            System.out.print(n[cont] + " ");
        }
        int pos = Arrays.binarySearch(n, 2);
        System.out.printf(" O valor 5 está na posição %d", pos);

        System.out.println();
        System.out.println("Total de casas de 'n' é " + n.length);

        for(int cont = 0; cont < n.length; cont++) {
            System.out.printf("Na posição %d temos o valor %d\n", cont, n[cont]);
        }

        System.out.println("Usando forEach");
        Arrays.sort(n);
        // Aqui o laço ocorre com a variável valor recebendo o conteúdo de cada indíce do vetor automaticamente
        for(int valor: n) {
            System.out.print(valor + " ");
        }
        System.out.println();

        int[] auto = new int[5];
        Arrays.fill(auto, 8);
        for(int a = 0; a < auto.length; a++) {
            System.out.print(auto[a] + " ");
        }
    }
}
