package array_java;

//9. Rotate Array to the Right by K Steps:
// Algorithm:
// Calculate the effective rotation by taking the remainder when dividing k by the array length (k % arr.length).
// Reverse the entire array.
// Reverse the subarray from index 0 to k - 1.
// Reverse the subarray from index k to the end of the array.
public class RotateArray {
  public static void main(String[] args) {
      int[] numbers = {1, 2, 3, 4, 5};
      int k = 2;
rotateArray(numbers, k);
      for (int num : numbers) {
          System.out.print(num + " ");
      }
  }
  private static void rotateArray(int[] arr, int k) {
      k = k % arr.length;
      reverse(arr, 0, arr.length - 1);
      reverse(arr, 0, k - 1);
      reverse(arr, k, arr.length - 1);
  }
  private static void reverse(int[] arr, int start, int end) {
      while (start < end) {
          int temp = arr[start];
          arr[start] = arr[end];
          arr[end] = temp;
          start++;
          end--;
      }
  }
}
