package array_java;

//16. Find Subarray with Given Sum:
//Algorithm:
//Initialize variables start and end to track the current subarray.
//Initialize variables currentSum and targetSum to 0 and the given sum, respectively.
//Iterate through the array.
//Add the current element to currentSum.
//If currentSum becomes greater than targetSum, remove elements from the beginning of the subarray until currentSum becomes less than or equal to targetSum.
//If currentSum becomes equal to targetSum, print the indices of the subarray.
//Repeat until the end of the array.

public class SubarrayWithGivenSum {
    public static void main(String[] args) {
        int[] numbers = {1, 4, 20, 3, 10, 5};
        int targetSum = 33;
findSubarrayWithSum(numbers, targetSum);
    }
    private static void findSubarrayWithSum(int[] arr, int targetSum) {
        int start = 0, end = 0, currentSum = 0;
        while (end < arr.length) {
            currentSum += arr[end];
            while (currentSum > targetSum && start <= end) {
                currentSum -= arr[start];
                start++;
            }
            if (currentSum == targetSum) {
                System.out.println("Subarray found between indices " + start + " and " + end);
                return;
            }
            end++;
        }
        System.out.println("No subarray found with the given sum.");
    }
}
