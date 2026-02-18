import java.util.*;

public class LongestConsecutiveSequenceInArray{

    public static void main(String[] args) {

        int[] nums = {100,4,200,1,3,2};   //{1,2,3,4}

        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;

        for (int num : set) {

            // Check if it is the start of a sequence
            if (!set.contains(num - 1)) {

                int currentNum = num;
                int count = 1;

                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    count++;
                }

                longest = Math.max(longest, count);
            }
        }

        System.out.println("Longest Sequence Length: " + longest);
    }
}
