package contadorswing;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ContadorSwing {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Contador");
        JPanel meuPainel = new JPanel();

        JLabel contagem = new JLabel("Contagem: ");
        JTextField txtContagem = new JTextField(10);
        JButton btnClick = new JButton("Contar");

        janela.setVisible(true);
        janela.setSize(300,266);

        janela.add(meuPainel);
        meuPainel.add(contagem);
        meuPainel.add(txtContagem);
        meuPainel.add(btnClick);

        btnClick.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int contador = 0;
                String mensagem = "";
                while(contador <= 5) {
                    mensagem += contador + " ";
                    txtContagem.setText(mensagem);
                    contador++;
                }
            }
        });
    }
}
