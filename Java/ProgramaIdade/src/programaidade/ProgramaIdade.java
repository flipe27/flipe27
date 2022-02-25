package programaidade;

import java.util.Scanner;

public class ProgramaIdade {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Qual seu ano de nascimento: ");
        int ano = teclado.nextInt();
        int idade = 2022 - ano;
        System.out.println("Sua idade é " + idade);

        if(idade >= 18) {
            System.out.println("Maior de idade!");
        } else {
            System.out.println("Menor de idade!");
        }
    }
}
