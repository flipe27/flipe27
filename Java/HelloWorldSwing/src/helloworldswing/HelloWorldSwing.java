package helloworldswing;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HelloWorldSwing {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Janela");
        JPanel meuPainel = new JPanel();
        JLabel lblMensagem = new JLabel("Aqui vai aparecer a Mensagem");
        JButton btnClick = new JButton("Clique em mim!");

        janela.setSize(300, 266);
        janela.setVisible(true);

        janela.add(meuPainel);
        meuPainel.add(lblMensagem);
        meuPainel.add(btnClick);

        btnClick.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                lblMensagem.setText("Hello, World!");
            }
        });
    }
}
