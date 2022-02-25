package verificadoridadeswing;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VerificadorIdadeSwing {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Cálculo de idade");
        JPanel meuPainel = new JPanel();

        JLabel lblAno = new JLabel("Ano de Nascimento");
        JTextField ano = new JTextField(10);
        JButton btnClick = new JButton("Calcular Idade");
        JLabel lblIdade = new JLabel("Idade: ");
        JLabel resIdade = new JLabel("0");
        JLabel situacao = new JLabel("Situação do voto: ");
        JLabel resSituacao = new JLabel("<vazio>");

        janela.setVisible(true);
        janela.setSize(300, 266);
        janela.add(meuPainel);

        meuPainel.add(lblAno);
        meuPainel.add(ano);
        meuPainel.add(btnClick);
        meuPainel.add(lblIdade);
        meuPainel.add(resIdade);
        meuPainel.add(situacao);
        meuPainel.add(resSituacao);

        btnClick.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int anoNasc = Integer.parseInt(ano.getText());
                int idade = 2022 - anoNasc;
                resIdade.setText(Integer.toString(idade));

                if(idade < 16) {
                    resSituacao.setText("Não vota!");
                } else if((idade >= 16 && idade < 18) || idade > 70) {
                    resSituacao.setText("Voto opcional!");
                } else {
                    resSituacao.setText("Voto obrigatório!");
                }
            }
        });
    }
}
