package array_java;

public class LinearSearch {
	public static void main(String[] args) {
        int[] numbers = {5, 8, 2, 1, 9, 3};
        int target = 9;
int index = linearSearch(numbers, target);
        if (index != -1) {
            System.out.println("Element found at index: " + index);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
    private static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

}
