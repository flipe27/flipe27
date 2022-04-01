package aula08;

public class Aula08 {
    public static void main(String[] args) {
        Pessoa[] p = new Pessoa[2];
        Livro[] l = new Livro[3];

        p[0] = new Pessoa("Kazuki", 19, "M");
        p[1] = new Pessoa("Chlóe", 19, "F");

        l[0] = new Livro("One Piece", "Eichiro Oda", 1000, p[0]);
        l[1] = new Livro("Haikyuu", "Haruichi Furudate", 85, p[1]);
        l[2] = new Livro("Fulllmetal ALchemist", "Hiromu Arakawa", 64, p[1]);

        l[0].abrir();
        l[0].folhear(1001);
        l[0].avancarPag();
        System.out.println(l[0].detalhes());
    }
}
