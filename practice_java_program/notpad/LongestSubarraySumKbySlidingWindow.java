public class LongestSubarraySumKbySlidingWindow{

    public static void main(String[] args) {

        int[] arr = {1,2,3,1,1,1,1};
        int k = 3;

        int left = 0, sum = 0, maxLen = 0;
        int startIndex = 0;   // to store start of max subarray

        for (int right = 0; right < arr.length; right++) {

            sum += arr[right];

            while (sum > k) {
                sum -= arr[left];
                left++;
            }

            if (sum == k) {
                if (right - left + 1 > maxLen) {
                    maxLen = right - left + 1;
                    startIndex = left;   // store start
                }
            }
        }

        System.out.println("Longest Length: " + maxLen);

        if (maxLen > 0) {
            System.out.print("Subarray: ");
            for (int i = startIndex; i < startIndex + maxLen; i++) {
                System.out.print(arr[i] + " ");
            }
        }
    }
}
