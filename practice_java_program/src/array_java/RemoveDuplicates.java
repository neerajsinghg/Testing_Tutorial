package array_java;

//7. Remove Duplicate Elements from an Array:
// Algorithm:
// Initialize an empty set to keep track of unique elements.
// Iterate through each element in the array.
// If the element is not in the set, add it to the set and print it.
import java.util.HashSet;
public class RemoveDuplicates {
  public static void main(String[] args) {
      int[] numbers = {3, 7, 2, 8, 7, 3, 1, 2};
removeDuplicates(numbers);
  }
  private static void removeDuplicates(int[] arr) {
      HashSet<Integer> uniqueSet = new HashSet<>();
      for (int num : arr) {
          if (uniqueSet.add(num)) {
              System.out.print(num + " ");
          }
      }
  }
}
