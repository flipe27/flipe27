package aula10;

public class Aula10 {
    public static void main(String[] args) {
        // Programa principal
        Visitante p1 = new Visitante("Paulo", 21, "M");
        Aluno p2 = new Aluno("Débora", 22, "F", 1111, "Informática");
        Bolsista p3 = new Bolsista("Bibi", 4, "F", 1111, "Veterinária", 1111f);

        System.out.println(p1);  // Chama automaticamente o "toString()"
        p2.pagarMensalidade();
        p3.pagarMensalidade();
    }
}
