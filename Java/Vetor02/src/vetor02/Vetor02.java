package vetor02;

public class Vetor02 {
    public static void main(String[] args) {
        String[] mes = {"Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"};
        int[] dias = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int anoAtual = 2022;
        if(anoAtual % 4 == 0) {
            dias[1] = 29;
        }

        for(int contador = 0; contador < mes.length; contador++) {
            System.out.printf("O mês de %s tem %d dias\n", mes[contador], dias[contador]);
        }
    }
}
