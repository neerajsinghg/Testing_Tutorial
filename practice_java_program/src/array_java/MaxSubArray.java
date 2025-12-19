package array_java;
//17. Largest Sum Contiguous Subarray (Kadane’s Algorithm):
//Find the sum of the contiguous subarray with the largest sum.
public class MaxSubArray {
	public int maxSubArray(int[] nums) {
	     int maxSum = nums[0];
	     int currentSum = nums[0];
	 for (int i = 1; i < nums.length; i++) {
	         currentSum = Math.max(nums[i], currentSum + nums[i]);
	         maxSum = Math.max(maxSum, currentSum);
	     }
	     return maxSum;
	 }

}
