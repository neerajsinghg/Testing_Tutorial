package array_java;

public class ReverseArray {
	public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int start = 0;
        int end = numbers.length - 1;
		while (start < end) {
		            // Swap elements at start and end indices
		            int temp = numbers[start];
		            numbers[start] = numbers[end];
		            numbers[end] = temp;
		            // Move indices towards the center
		            start++;
		            end--;
		        }
		        // Print reversed array
		        for (int num : numbers) {
		            System.out.print(num + " ");
		        }
		    }

}
