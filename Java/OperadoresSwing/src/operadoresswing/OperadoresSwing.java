package operadoresswing;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class OperadoresSwing {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Divisão e Resto");
        JPanel meuPainel = new JPanel();


        JLabel n1 = new JLabel("Numerador");
        JLabel n2 = new JLabel("Denominador");
        JTextField txtN1 = new JTextField(10);
        JTextField txtN2 = new JTextField(10);
        JButton btnClick = new JButton("Dividir");
        JLabel divisao = new JLabel("Divisão: ");
        JLabel resto = new JLabel("Resto: ");
        JLabel resDivisao = new JLabel("0 ");
        JLabel resResto = new JLabel("0");

        janela.setVisible(true);
        janela.setSize(300, 266);

        janela.add(meuPainel);
        meuPainel.add(n1);
        meuPainel.add(txtN1);
        meuPainel.add(n2);
        meuPainel.add(txtN2);
        meuPainel.add(btnClick);
        meuPainel.add(divisao);
        meuPainel.add(resDivisao);
        meuPainel.add(resto);
        meuPainel.add(resResto);

        btnClick.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                float num = Float.parseFloat(txtN1.getText());
                float dem = Float.parseFloat(txtN2.getText());

                float div = num / dem;
                float res = num % dem;

                resDivisao.setText(Float.toString(div));
                resResto.setText(Float.toString(res));
            }
        });
    }
}
