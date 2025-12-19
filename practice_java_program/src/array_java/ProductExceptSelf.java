package array_java;
//18. Array Product Except Self:
//Algorithm:
//Calculate the product of all elements to the left of each element.
//Calculate the product of all elements to the right of each element.
//Multiply the left and right products for each element to get the final result.
public class ProductExceptSelf {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4};
int[] result = productExceptSelf(numbers);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
    private static int[] productExceptSelf(int[] arr) {
        int n = arr.length;
        int[] leftProducts = new int[n];
        int[] rightProducts = new int[n];
        int[] result = new int[n];
        leftProducts[0] = 1;
        for (int i = 1; i < n; i++) {
            leftProducts[i] = leftProducts[i - 1] * arr[i - 1];
        }
        rightProducts[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            rightProducts[i] = rightProducts[i + 1] * arr[i + 1];
        }
        for (int i = 0; i < n; i++) {
            result[i] = leftProducts[i] * rightProducts[i];
        }
        return result;
    }
}
