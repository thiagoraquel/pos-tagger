import java.util.Scanner;

public class AnaliseDeValores {
  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    int totalValores = 0;
    int positivos = 0;
    int negativos = 0;
    double soma = 0;
    
    System.out.println("Digite valores numéricos (digite 0 para encerrar):");
    while (true) {
      System.out.print("Valor ");
      double valor = in.nextDouble();

      if (valor == 0) {
        break;
      }

      soma += valor;
      totalValores++;

      if (valor > 0) {
        positivos++;
      } else {
        negativos++;
      }
    
    }

    if (totalValores == 0) {
      System.out.println("Nenhum valor foi inserido.");
    } else {
      double media = soma /totalValores;
      double percentualPos = (positivos * 100.0) / totalValores;
      double percentualNeg = (negativos * 100.0) / totalValores;

      System.out.println("\nResultados:");
      System.out.println("Média dos valores: " + media);
      System.out.println("Quantidade de positivos: " + positivos);
      System.out.println("Quantidade de negativos: " + negativos);
      System.out.println("Percentual de positivos: " + percentualPos + "%");
      System.out.println("Percentual de negativos: " + percentualNeg + "%");
    }

    in.close();
  }

}
