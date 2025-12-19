package array_java;

//10. Find Leaders in an Array:
//Algorithm:
//Initialize a variable max to the last element of the array.
//Iterate through the array from right to left.
//For each element, if it’s greater than max, update max and print the element.
public class LeadersInArray {
  public static void main(String[] args) {
      int[] numbers = {16, 17, 4, 3, 5, 2};
findLeaders(numbers);
  }
  private static void findLeaders(int[] arr) {
      int max = arr[arr.length - 1];
      System.out.println("Leader: " + max);
      for (int i = arr.length - 2; i >= 0; i--) {
          if (arr[i] > max) {
              max = arr[i];
              System.out.println("Leader: " + max);
          }
      }
  }
}
