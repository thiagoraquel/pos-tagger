public class SomaImparesMultiplosDeTres {
  public static void main(String[] args) {
      int soma = 0;

      for (int i = 1; i <= 500; i++) {
          if (i % 2 != 0 && i % 3 == 0) { // número ímpar e múltiplo de 3
              soma += i;
          }
      }

      System.out.println("A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: " + soma);
  }
}
