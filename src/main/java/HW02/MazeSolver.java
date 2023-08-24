package HW02;

public class MazeSolver {
    private static final int WALL = 1;
    private static final int PATH = 2;

    public static void main(String[] args) {
        int[][] maze = {
                {0, 1, 0, 0},
                {0, 1, 0, 1},
                {0, 0, 0, 0},
                {0, 1, 1, 0}
        };

        int startX = 0;
        int startY = 0;
        int endX = 3;
        int endY = 3;

        if (solveMaze(maze, startX, startY, endX, endY)) {
            System.out.println("Путь найден!");
        } else {
            System.out.println("Путь не найден");
        }
    }

    private static boolean solveMaze(int[][] maze, int currentX, int currentY, int endX, int endY) {
        if (currentX == endX && currentY == endY) {
            return true;
        }

        if (isValid(maze, currentX, currentY)) {
            maze[currentX][currentY] = PATH;

            // двигаемся вправо
            if (solveMaze(maze, currentX + 1, currentY, endX, endY)) {
                return true;
            }

            // двигаемся вниз
            if (solveMaze(maze, currentX, currentY + 1, endX, endY)) {
                return true;
            }

            // двигаемся влево
            if (solveMaze(maze, currentX - 1, currentY, endX, endY)) {
                return true;
            }

            // двигаемся вверх
            if (solveMaze(maze, currentX, currentY - 1, endX, endY)) {
                return true;
            }


            maze[currentX][currentY] = 0;
        }

        return false;
    }

    private static boolean isValid(int[][] maze, int x, int y) {
        int rows = maze.length;
        int columns = maze[0].length;


        return x >= 0 && x < rows && y >= 0 && y < columns && maze[x][y] == 0;
    }
}
