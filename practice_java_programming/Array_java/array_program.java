1. Sum of Elements in an Array:
Algorithm:

Initialize a variable sum to 0.
Iterate through each element in the array.
Add each element to the sum.
Print the final sum.
public class SumOfArray {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;
for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum of elements: " + sum);
    }
}
2. Find Maximum and Minimum in an Array:
Algorithm:

Initialize variables max and min with the first element of the array.
Iterate through each element in the array.
If the current element is greater than max, update max.
If the current element is less than min, update min.
Print the final values of max and min.
public class MaxMinArray {
    public static void main(String[] args) {
        int[] numbers = {7, 2, 9, 1, 5};
        int max = numbers[0];
        int min = numbers[0];
for (int num : numbers) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
    }
}
3. Check if Array Contains a Specific Element:
Algorithm:

Initialize a boolean variable contains to false.
Iterate through each element in the array.
If the current element is equal to the target element, set contains to true and break out of the loop.
Print whether the array contains the target element based on the value of contains.
public class ArrayContainsElement {
    public static void main(String[] args) {
        int[] numbers = {3, 6, 9, 12, 15};
        int target = 9;
        boolean contains = false;
for (int num : numbers) {
            if (num == target) {
                contains = true;
                break;
            }
        }
        if (contains) {
            System.out.println("Array contains " + target);
        } else {
            System.out.println("Array does not contain " + target);
        }
    }
}
4. Reverse an Array:
Algorithm:

Initialize variables start to 0 and end to the last index of the array.
Use a while loop with the condition start < end to swap elements at positions start and end.
Increment start and decrement end in each iteration.
Print the reversed array.
public class ReverseArray {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int start = 0;
        int end = numbers.length - 1;
while (start < end) {
            // Swap elements at start and end indices
            int temp = numbers[start];
            numbers[start] = numbers[end];
            numbers[end] = temp;
            // Move indices towards the center
            start++;
            end--;
        }
        // Print reversed array
        for (int num : numbers) {
            System.out.print(num + " ");
        }
    }
}
5. Linear Search: Find Index of an Element in an Array:
Algorithm:

Initialize a variable target with the element to search.
Iterate through each element in the array.
If the current element is equal to the target, return the current index.
If the loop completes without finding the element, return -1.
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
6. Check if an Array is Sorted:
Algorithm:

Iterate through each element in the array.
Compare the current element with the next element.
If any element is greater than the next one, the array is not sorted.
If the loop completes without finding such elements, the array is sorted.
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
7. Remove Duplicate Elements from an Array:
Algorithm:

Initialize an empty set to keep track of unique elements.
Iterate through each element in the array.
If the element is not in the set, add it to the set and print it.
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
8. Count Occurrences of Each Element in an Array:
Algorithm:

Initialize a HashMap to store element frequencies.
Iterate through each element in the array.
For each element, update its frequency in the HashMap.
Print the element and its frequency.
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
9. Rotate Array to the Right by K Steps:
Algorithm:

Calculate the effective rotation by taking the remainder when dividing k by the array length (k % arr.length).
Reverse the entire array.
Reverse the subarray from index 0 to k - 1.
Reverse the subarray from index k to the end of the array.
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
10. Find Leaders in an Array:
Algorithm:

Initialize a variable max to the last element of the array.
Iterate through the array from right to left.
For each element, if it’s greater than max, update max and print the element.
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
11. Find the Missing Number:
Given an array containing n distinct numbers taken from the range 0 to n, find the one missing from the array.
Calculate the expected sum of the first n natural numbers using the formula n * (n + 1) / 2
Calculate the actual sum of the elements in the array using a ‘for’ loop.
Subtract the actual sum from the expected sum.
The result is the missing number.
public int findMissingNumber(int[] nums) {
    int n = nums.length + 1;
    int expectedSum = n * (n + 1) / 2;
    int actualSum = 0;
for (int num : nums) {
        actualSum += num;
    }
    return expectedSum - actualSum;
}
12. Remove Duplicates from Sorted Array:
Remove the duplicates in a sorted array, modifying the array in-place.

Algorithm:

Initialize a variable uniqueIndex to 0.
Iterate through the array from index 1.
If the current element is different from the element at uniqueIndex, increment uniqueIndex and update the element at that index.
Continue the iteration until the end of the array.
The unique elements are now in the subarray nums[0] to nums[uniqueIndex].
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) {
        return 0;
    }
int uniqueIndex = 0;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] != nums[uniqueIndex]) {
            uniqueIndex++;
            nums[uniqueIndex] = nums[i];
        }
    }
    return uniqueIndex + 1;
}
13. Rotate Array:
Rotate an array to the right by k steps.

Algorithm:

Calculate the effective rotation by taking the remainder when dividing k by the array length (k % nums.length).
Reverse the entire array.
Reverse the subarray from index 0 to k - 1.
Reverse the subarray from index k to the end of the array.
public void rotateArray(int[] nums, int k) {
    k = k % nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
}
private void reverse(int[] nums, int start, int end) {
    while (start < end) {
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}
14. Find Second Largest Element in an Array:
Algorithm:

Initialize variables max and secondMax to Integer.MIN_VALUE.
Iterate through each element in the array.
If the current element is greater than max, update secondMax to max and max to the current element.
If the current element is greater than secondMax but less than max, update secondMax to the current element.
Print the value of secondMax.
public class SecondLargestElement {
    public static void main(String[] args) {
        int[] numbers = {5, 8, 2, 1, 9, 3};

int secondLargest = findSecondLargest(numbers);
        System.out.println("Second Largest Element: " + secondLargest);
    }
    private static int findSecondLargest(int[] arr) {
        int max = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;
        for (int num : arr) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax && num != max) {
                secondMax = num;
            }
        }
        return secondMax;
    }
}
15. Merge Two Sorted Arrays:
Algorithm:

Initialize an empty array to store the merged result.
Initialize pointers i, j, and k to 0 to track the positions in the two input arrays and the merged array, respectively.
Compare elements from both arrays and add the smaller one to the merged array.
Increment the pointer of the array from which the element was added and the pointer for the merged array.
Repeat until both input arrays are completely traversed.
Copy any remaining elements from either array to the merged array.
Return the merged array.
public class MergeSortedArrays {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 5, 7};
        int[] arr2 = {2, 4, 6, 8};
int[] mergedArray = mergeArrays(arr1, arr2);
        System.out.println("Merged Array:");
        for (int num : mergedArray) {
            System.out.print(num + " ");
        }
    }
    private static int[] mergeArrays(int[] arr1, int[] arr2) {
        int[] mergedArray = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                mergedArray[k++] = arr1[i++];
            } else {
                mergedArray[k++] = arr2[j++];
            }
        }
        while (i < arr1.length) {
            mergedArray[k++] = arr1[i++];
        }
        while (j < arr2.length) {
            mergedArray[k++] = arr2[j++];
        }
        return mergedArray;
    }
}
16. Find Subarray with Given Sum:
Algorithm:

Initialize variables start and end to track the current subarray.
Initialize variables currentSum and targetSum to 0 and the given sum, respectively.
Iterate through the array.
Add the current element to currentSum.
If currentSum becomes greater than targetSum, remove elements from the beginning of the subarray until currentSum becomes less than or equal to targetSum.
If currentSum becomes equal to targetSum, print the indices of the subarray.
Repeat until the end of the array.
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
17. Largest Sum Contiguous Subarray (Kadane’s Algorithm):
Find the sum of the contiguous subarray with the largest sum.

public int maxSubArray(int[] nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];
for (int i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}
18. Array Product Except Self:
Algorithm:

Calculate the product of all elements to the left of each element.
Calculate the product of all elements to the right of each element.
Multiply the left and right products for each element to get the final result.
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
19. Find Maximum Product Subarray:
Algorithm:

Initialize maxProduct and minProduct to the first element.
Initialize result to the first element.
Traverse the array:
If the current element is negative, swap maxProduct and minProduct.
Update maxProduct and minProduct by considering the current element.
Update result with the maximum value.
4.Return result.

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
20. Dutch National Flag Problem (Sort an Array of 0s, 1s, and 2s):
Given an array A [] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array.

Algorithm:

Initialize three pointers: low, mid, and high.
Traverse the array:
If the current element is 0, swap it with the element at the low pointer and increment both low and mid.
If the current element is 1, just increment mid.
If the current element is 2, swap it with the element at the high pointer and decrement high.
3. Continue until mid crosses high.

public class DutchNationalFlag {
    public static void main(String[] args) {
        int[] arr = {2, 0, 1, 2, 1, 0, 1, 0, 2};
sortColors(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
    private static void sortColors(int[] arr) {
        int low = 0;
        int mid = 0;
        int high = arr.length - 1;
        while (mid <= high) {
            switch (arr[mid]) {
                case 0:
                    swap(arr, low, mid);
                    low++;
                    mid++;
                    break;
                case 1:
                    mid++;
                    break;
                case 2:
                    swap(arr, mid, high);
                    high--;
                    break;
            }
        }
    }
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}


Q1. What’s the difference between Arrays.asList() and List.of()?