package testefuncao02;

public class Operacoes {
    public static String contador(int i, int f) {
        String s = "";
        for(int j = i; j <= f; j++) {
            s += j + " ";
        }
        return s;
    }
}
