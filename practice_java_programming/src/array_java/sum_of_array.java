package array_java;
// 1. Sum of Elements in an Array:
// Initialize a variable sum to 0.
// Iterate through each element in the array.
// Add each element to the sum.
// Print the final sum.

public class sum_of_array {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;
for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum of elements: " + sum);
    }

}
