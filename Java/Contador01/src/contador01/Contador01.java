package contador01;

public class Contador01 {
    public static void main(String[] args) {
        int contador = 0;
        while(contador < 10) {
            contador++;
            if(contador == 5 || contador == 7) {
                continue;
            }
            if(contador == 9) {
                break;
            }
            System.out.println("Cambalhota " + contador);
        }
    }
}
