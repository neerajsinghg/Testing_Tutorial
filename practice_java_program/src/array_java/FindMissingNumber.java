package array_java;

//11. Find the Missing Number:
//Given an array containing n distinct numbers taken from the range 0 to n, find the one missing from the array.
//Calculate the expected sum of the first n natural numbers using the formula n * (n + 1) / 2
//Calculate the actual sum of the elements in the array using a ‘for’ loop.
//Subtract the actual sum from the expected sum.
//The result is the missing number.
//Option 1: Static Method Approach

public class FindMissingNumber {
    
    // Method to find missing number
    public static int findMissingNumber(int[] nums) {
        int n = nums.length; // For array containing numbers 0 to n, length should be n
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }
    
    public static void main(String[] args) {
        // Test cases
        int[] testArray1 = {0, 1, 2, 4, 5}; // Missing 3
        int[] testArray2 = {3, 0, 1}; // Missing 2
        int[] testArray3 = {0, 1, 2, 3, 4, 5, 6, 8, 9}; // Missing 7
        
        System.out.println("Missing number in array 1: " + findMissingNumber(testArray1));
        System.out.println("Missing number in array 2: " + findMissingNumber(testArray2));
        System.out.println("Missing number in array 3: " + findMissingNumber(testArray3));
    }
}

////Option 2: Instance Method Approach
//
//public class FindMissingNumber {
//    
//    // Instance method
//    public int findMissingNumber(int[] nums) {
//        int n = nums.length;
//        int expectedSum = n * (n + 1) / 2;
//        int actualSum = 0;
//        
//        for (int num : nums) {
//            actualSum += num;
//        }
//        return expectedSum - actualSum;
//    }
//    
//    public static void main(String[] args) {
//        FindMissingNumber finder = new FindMissingNumber();
//        
//        // Test cases
//        int[] testArray1 = {0, 1, 2, 4, 5}; // Missing 3
//        int[] testArray2 = {3, 0, 1}; // Missing 2
//        int[] testArray3 = {0, 1, 2, 3, 4, 5, 6, 8, 9}; // Missing 7
//        
//        System.out.println("Missing number in array 1: " + finder.findMissingNumber(testArray1));
//        System.out.println("Missing number in array 2: " + finder.findMissingNumber(testArray2));
//        System.out.println("Missing number in array 3: " + finder.findMissingNumber(testArray3));
//    }
//}