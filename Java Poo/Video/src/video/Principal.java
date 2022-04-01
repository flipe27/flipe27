package video;

public class Principal {
    public static void main(String[] args) {
        // Programa principal
        Video[] v = new Video[3];
        v[0] = new Video("Aula 01 de JavaScript");
        v[1] = new Video("Aula 10 de Python");

        Gafanhoto[] g = new Gafanhoto[2];
        g[0] = new Gafanhoto("Isshiki Kazuki", "M", 19, "Kuro Saber");
        g[1] = new Gafanhoto("Chlóe Maillé", "F", 19, "Apprentice");

        Visualizacao[] vis = new Visualizacao[2];
        vis[0] = new Visualizacao(g[0], v[0]);
        vis[1] = new Visualizacao(g[1], v[0]);

        vis[0].avaliar();
        vis[1].avaliar(10);

        System.out.println("--------- VIDEOS ---------");
        System.out.println(v[0] + "\n");
        System.out.println(v[1]);
        System.out.println("------- GAFANHOTOS -------");
        System.out.println(g[0] + "\n");
        System.out.println(g[1]);
    }
}
