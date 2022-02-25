package testefuncao01;

public class TesteFuncao01 {
    static void soma(int a, int b) {
        int s = a + b;
        System.out.println("A soma é " + s);
    }

    static int somaReturn(int c, int d) {
        return c + d;
    }

    public static void main(String[] args) {
        soma(5,2);

        int sum = somaReturn(12, 27);
        System.out.println("A soma é " + sum);
    }
}
