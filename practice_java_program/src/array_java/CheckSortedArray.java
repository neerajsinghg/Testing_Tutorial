package array_java;
//6. Check if an Array is Sorted:
// Algorithm:
// Iterate through each element in the array.
// Compare the current element with the next element.
// If any element is greater than the next one, the array is not sorted.
// If the loop completes without finding such elements, the array is sorted.
public class CheckSortedArray {
    public static void main(String[] args) {
        int[] numbers = {1, 3, 5, 7, 9};
if (isSorted(numbers)) {
            System.out.println("The array is sorted.");
        } else {
            System.out.println("The array is not sorted.");
        }
    }
    private static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }

}
