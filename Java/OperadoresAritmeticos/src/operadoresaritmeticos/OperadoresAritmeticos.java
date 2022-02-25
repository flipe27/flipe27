package operadoresaritmeticos;

public class OperadoresAritmeticos {
    public static void main(String[] args) {
        float n1 = 3f;
        float n2 = 5f;
        float m = (n1 + n2) / 2;
        System.out.printf("A média é igual a %.1f\n", m);

        int numero = 5;
        int valor = 5 + numero++;  // Acontece um pós-incremento
        // int preValor = 5 + ++numero;  Acontece um pré-incremento
        System.out.println(valor);
        System.out.println(numero);

        int x = 4;
        x *= 2;
        System.out.println(x);

        double pi = Math.PI;
        double resultado = Math.pow(pi, 3);
        int absoluto = -10;
        System.out.printf("A raiz quadrada de %.6f ao cubo é igual a %.6f\n", pi, Math.sqrt(resultado));
        System.out.println(Math.abs(absoluto));

        float arredondado = 8.5f;
        System.out.printf("%.1f arredondado para cima é igual a %.1f\n", arredondado, Math.floor(arredondado));
        System.out.printf("%.1f arredondado para baixo é igual a %.1f\n", arredondado, Math.ceil(arredondado));
        System.out.printf("%.1f arredondado aritméticamente é igual a %d\n", arredondado, Math.round(arredondado));
    }
}
