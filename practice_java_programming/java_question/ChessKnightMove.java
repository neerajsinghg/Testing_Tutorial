package java_question;
import java.util.Scanner;

	public class ChessKnightMove {
	    @SuppressWarnings("resource")
		public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);

	        // Get starting position
	        System.out.print("Enter starting X coordinate (1-8): ");
	        int x = scanner.nextInt();
	        System.out.print("Enter starting Y coordinate (1-8): ");
	        int y = scanner.nextInt();

	        // Check if input is within the board limits
	        if (x < 1 || x > 8 || y < 1 || y > 8) {
	            System.out.println("Invalid input! Coordinates should be between 1 and 8.");
	            return;
	        }

	        System.out.println("\nPossible moves for Knight from (" + x + ", " + y + "):");

	        // Possible moves of a knight in chess
	        int[][] moves = {
	            {2, 1}, {2, -1}, {-2, 1}, {-2, -1},
	            {1, 2}, {1, -2}, {-1, 2}, {-1, -2}
	        };

	        // Check and display valid moves
	        for (int[] move : moves) {
	            int newX = x + move[0];
	            int newY = y + move[1];

	            if (newX >= 1 && newX <= 8 && newY >= 1 && newY <= 8) {
	                System.out.println("(" + newX + ", " + newY + ")");
	            }
	        }

	        scanner.close();
	    }
	}
