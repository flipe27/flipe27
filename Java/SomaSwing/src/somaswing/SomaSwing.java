package somaswing;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SomaSwing {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Soma");
        JPanel meuPainel = new JPanel();
        JTextField txtN1 = new JTextField(5);
        JTextField txtN2 = new JTextField(5);
        JLabel plus = new JLabel("+");
        JLabel lblResultado = new JLabel("0");
        JButton btnSoma = new JButton("=");

        janela.setVisible(true);
        janela.setSize(300, 266);

        janela.add(meuPainel);
        meuPainel.add(txtN1);
        meuPainel.add(plus);
        meuPainel.add(txtN2);
        meuPainel.add(btnSoma);
        meuPainel.add(lblResultado);

        btnSoma.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int n1 = Integer.parseInt(txtN1.getText());
                int n2 = Integer.parseInt(txtN2.getText());
                int soma = n1 + n2;

                lblResultado.setText(Integer.toString(soma));
            }
        });
    }
}
