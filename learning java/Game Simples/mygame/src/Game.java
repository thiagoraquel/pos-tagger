public class Game {
  private final int WIDTH = 5;
  private final int HEIGHT = 5;
  private Player player;
  private final int goalX = 4;
  private final int goalY = 4;

  public Game() {
      player = new Player(0, 0);
  }

  public void render() {
      for (int y = 0; y < HEIGHT; y++) {
          for (int x = 0; x < WIDTH; x++) {
              if (player.getX() == x && player.getY() == y) {
                  System.out.print("P ");
              } else if (x == goalX && y == goalY) {
                  System.out.print("X ");
              } else {
                  System.out.print(". ");
              }
          }
          System.out.println();
      }
  }

  public void update(String direction) {
      int newX = player.getX();
      int newY = player.getY();

      switch (direction) {
          case "w": newY--; break;
          case "s": newY++; break;
          case "a": newX--; break;
          case "d": newX++; break;
          default: break; // entrada inválida não faz nada
      }

      if (isInsideMap(newX, newY)) {
          player.setPosition(newX, newY);
      }
  }

  public boolean isGameOver() {
      return player.getX() == goalX && player.getY() == goalY;
  }

  private boolean isInsideMap(int x, int y) {
      return x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT;
  }
}
