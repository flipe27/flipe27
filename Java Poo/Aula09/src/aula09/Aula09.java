package aula09;

public class Aula09 {
    public static void main(String[] args) {
        // Programa principal
        Pessoa p1 = new Pessoa("Pedro", 18, "M");
        Aluno p2 = new Aluno("Maria", 20, "F", 10, "Informática");
        Professor p3 = new Professor("Cláudio", 38, "M", "Informática", 2500.75f);
        Funcionario p4 = new Funcionario("Fabiana", 30, "F", "Estoque", true);

        System.out.println(p4.toString());
    }
}
