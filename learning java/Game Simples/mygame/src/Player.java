public class Player {
  private int x, y;

  public Player(int startX, int startY) {
      this.x = startX;
      this.y = startY;
  }

  public int getX() {
      return x;
  }

  public int getY() {
      return y;
  }

  public void setPosition(int newX, int newY) {
      this.x = newX;
      this.y = newY;
  }
}
