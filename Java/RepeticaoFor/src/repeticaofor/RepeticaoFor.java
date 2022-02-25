package repeticaofor;

public class RepeticaoFor {
    public static void main(String[] args) {
        for(int contador = 0; contador <= 3; contador++) {
            System.out.println("Cambalhota " + (contador + 1));
        }

        for(int volta = 15; volta >= 5; volta -= 2) {
            System.out.println("Voltando " + volta);
        }

        String frase = "";
        for(int ate100 = 0; ate100 <= 100; ate100 += 10) {
            frase += "Contando " + ate100 + " ";
        }
        System.out.println(frase);

        for(int i = 1; i <= 3; i++) {
            for(int j = 0; j <= 2; j++) {
                System.out.println(i + " " + j);
            }
        }
    }
}
