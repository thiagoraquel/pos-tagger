import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPClient {
    public static void main(String[] args) throws IOException {
        String servidor = "localhost";
        int porta = 12345;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nEscolha a operação:");
            System.out.println("1 - SOMA");
            System.out.println("2 - SUBTRAÇÃO");
            System.out.println("3 - MULTIPLICAÇÃO");
            System.out.println("4 - DIVISÃO INTEIRA");
            System.out.println("0 - SAIR");

            System.out.print("Digite o número da operação: ");
            String opcaoStr = scanner.nextLine().trim();

            if (opcaoStr.equals("0") || opcaoStr.equalsIgnoreCase("sair")) {
                System.out.println("Encerrando o cliente...");
                break;
            }

            int opcao;
            try {
                opcao = Integer.parseInt(opcaoStr);
            } catch (NumberFormatException e) {
                System.out.println("Entrada inválida. Digite um número de 0 a 4.");
                continue;
            }

            String operacao;
            switch (opcao) {
                case 1:
                    operacao = "SUM";
                    break;
                case 2:
                    operacao = "SUB";
                    break;
                case 3:
                    operacao = "MUL";
                    break;
                case 4:
                    operacao = "DIV";
                    break;
                default:
                    System.out.println("Opção inválida.");
                    continue;
            }

            try {
                System.out.print("Digite o primeiro número: ");
                int a = Integer.parseInt(scanner.nextLine());

                System.out.print("Digite o segundo número: ");
                int b = Integer.parseInt(scanner.nextLine());

                String mensagem = operacao + ":" + a + ":" + b;

                Socket socket = new Socket(servidor, porta);
                BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter saida = new PrintWriter(socket.getOutputStream(), true);

                System.out.println("Enviando: " + mensagem);
                saida.println(mensagem);

                String resposta = entrada.readLine();
                System.out.println("Resposta do servidor: " + resposta);

                socket.close();
            } catch (NumberFormatException e) {
                System.out.println("Erro: você deve digitar números inteiros válidos.");
            } catch (IOException e) {
                System.out.println("Erro de conexão com o servidor: " + e.getMessage());
            }
        }

        scanner.close();
    }
}
