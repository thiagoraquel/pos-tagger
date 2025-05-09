import java.io.*;
import java.net.*;

public class TCPServer {
    public static void main(String[] args) throws IOException {
        int porta = 12345;
        ServerSocket servidor = new ServerSocket(porta);
        System.out.println("Servidor TCP multithread ouvindo na porta " + porta);

        while (true) {
            Socket cliente = servidor.accept();
            System.out.println("Novo cliente conectado: " + cliente.getInetAddress());

            Thread clienteThread = new Thread(new TratadorCliente(cliente));
            clienteThread.start();
        }
    }
}

class TratadorCliente implements Runnable {
    private Socket cliente;

    public TratadorCliente(Socket cliente) {
        this.cliente = cliente;
    }

    @Override
    public void run() {
        try {
            BufferedReader entrada = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
            PrintWriter saida = new PrintWriter(cliente.getOutputStream(), true);

            String mensagem = entrada.readLine();
            System.out.println("Recebido de " + cliente.getInetAddress() + ": " + mensagem);

            String[] partes = mensagem.split(":");
            if (partes.length == 3) {
                try {
                    int a = Integer.parseInt(partes[1]);
                    int b = Integer.parseInt(partes[2]);
                    String operacao = partes[0];
                    int resultado;

                    switch (operacao) {
                        case "SUM":
                            resultado = a + b;
                            break;
                        case "SUB":
                            resultado = a - b;
                            break;
                        case "MUL":
                            resultado = a * b;
                            break;
                        case "DIV":
                            if (b == 0) {
                                saida.println("ERROR:Divisão por zero");
                                cliente.close();
                                return;
                            }
                            resultado = a / b;
                            break;
                        default:
                            saida.println("ERROR:Operação desconhecida");
                            cliente.close();
                            return;
                    }                    

                    saida.println("RESULT:" + resultado);
                } catch (NumberFormatException e) {
                    saida.println("ERROR:Formato inválido");
                }
            } else {
                saida.println("ERROR:Mensagem incompleta");
            }

            cliente.close();
        } catch (IOException e) {
            System.out.println("Erro ao tratar cliente: " + e.getMessage());
        }
    }
}
