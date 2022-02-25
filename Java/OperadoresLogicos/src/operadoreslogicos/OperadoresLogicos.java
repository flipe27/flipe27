package operadoreslogicos;

public class OperadoresLogicos {
    public static void main(String[] args) {
        int n1, n2, r;
        n1 = 4;
        n2 = 8;
        r = (n1 > n2) ? n1 : n2;  // Operação ternária, nesse caso se 'n1' > 'n2', 'r' = 'n1' se não, 'r' = 'n2'
        System.out.println(r);

        String nome1 = "Paulo";
        String nome2 = new String("Paulo");
        String resultado = (nome1 == nome2) ? "Igual" : "Diferente";
        String conteudo = (nome1.equals(nome2)) ? "Igual" : "Diferente";
        System.out.println(resultado);
        System.out.println(conteudo);

        int x, y, z;
        x = 4;
        y = 7;
        z = 12;
        boolean vOUf;
        vOUf = (x >= y && y < z) ? true : false;
        System.out.println(vOUf);
    }
}
