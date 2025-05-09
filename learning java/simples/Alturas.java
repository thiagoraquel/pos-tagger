import java.util.Scanner;

public class Alturas {
  public static void main(String[] args){
    Scanner entrada = new Scanner(System.in);
    double menor = 0, maior = 0;
    for(int i = 0; i < 5; i++){
      System.out.print("Altura " + (i + 1) + ": ");
      double altura = entrada.nextDouble();
      if (i == 0){
        menor = maior = altura;
      } else {
        if (altura < menor) menor = altura;
        if (altura > maior) maior = altura;
      }
    }

    System.out.println("Menor Altura: " + menor);
    System.out.println("Maior altura: " + maior);
    entrada.close();

  }
}