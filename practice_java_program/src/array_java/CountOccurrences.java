package array_java;

//8. Count Occurrences of Each Element in an Array:
// Algorithm:
// Initialize a HashMap to store element frequencies.
// Iterate through each element in the array.
// For each element, update its frequency in the HashMap.
// Print the element and its frequency.
import java.util.HashMap;
public class CountOccurrences {
  public static void main(String[] args) {
      int[] numbers = {3, 7, 2, 8, 7, 3, 1, 2};
      countOccurrences(numbers);
  }
  private static void countOccurrences(int[] arr) {
      HashMap<Integer, Integer> frequencyMap = new HashMap<>();
      for (int num : arr) {
          frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
      }
      for (int num : frequencyMap.keySet()) {
          System.out.println("Element: " + num + ", Frequency: " + frequencyMap.get(num));
      }
  }
}
