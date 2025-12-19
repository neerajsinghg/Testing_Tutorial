package array_java;
//19. Find Maximum Product Subarray:
//Algorithm:

//Initialize maxProduct and minProduct to the first element.
//Initialize result to the first element.
//Traverse the array:
//If the current element is negative, swap maxProduct and minProduct.
//Update maxProduct and minProduct by considering the current element.
//Update result with the maximum value.
//4.Return result.

public class MaxProductSubarray {
public static void main(String[] args) {
  int[] arr = {2, 3, -2, 4};
int maxProduct = findMaxProduct(arr);
  System.out.println("Maximum Product: " + maxProduct);
}
private static int findMaxProduct(int[] arr) {
  int maxProduct = arr[0];
  int minProduct = arr[0];
  int result = arr[0];
  for (int i = 1; i < arr.length; i++) {
      if (arr[i] < 0) {
          int temp = maxProduct;
          maxProduct = minProduct;
          minProduct = temp;
      }
      maxProduct = Math.max(arr[i], maxProduct * arr[i]);
      minProduct = Math.min(arr[i], minProduct * arr[i]);
      result = Math.max(result, maxProduct);
  }
  return result;
}
}
