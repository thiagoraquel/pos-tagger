import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Game game = new Game();
        Scanner in = new Scanner(System.in);

        while (!game.isGameOver()) {
            game.render();
            System.out.print("Digite a direção (w/a/s/d): ");
            String input = in.nextLine().toLowerCase();

            game.update(input);
        }

        game.render();
        System.out.println("Parabéns! Você alcançou a linha de chegada!");
        in.close();
    }
}

