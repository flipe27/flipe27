package programaparimparswing;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ProgramaParImparSwing {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Par ou Ímpar");
        JPanel meuPainel = new JPanel();

        JLabel valor = new JLabel("Valor");
        JTextField txtValor = new JTextField(10);
        JButton btnClick = new JButton("Verificar");
        JLabel resultado = new JLabel("Resultado");

        janela.setVisible(true);
        janela.setSize(300, 266);
        janela.add(meuPainel);

        meuPainel.add(valor);
        meuPainel.add(txtValor);
        meuPainel.add(btnClick);
        meuPainel.add(resultado);

        btnClick.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int numero = Integer.parseInt(txtValor.getText());
                if(numero % 2 == 0) {
                    resultado.setText("Par!");
                } else {
                    resultado.setText("Ímpar!");
                }
            }
        });
    }
}
