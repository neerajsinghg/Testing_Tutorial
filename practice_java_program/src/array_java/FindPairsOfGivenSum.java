package array_java;

import java.util.HashMap;
import java.util.Map;

public class FindPairsOfGivenSum {
    public static void main(String[] args) {
        int[] nums = new int[]{15, 12, 4, 16, 9, 8, 24, 0};
        int sum = 24;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            if (map.containsKey(sum - nums[i])) {
                System.out.println("pair found::" + (sum - nums[i]) + " " + nums[i]);
            }
            map.put(nums[i], i);
        }

    }
}
//output:
//pair found::15 9
//pair found::16 8