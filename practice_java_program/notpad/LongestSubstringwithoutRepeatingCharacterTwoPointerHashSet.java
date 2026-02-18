import java.util.*;

public class LongestSubstringwithoutRepeatingCharacterTwoPointerHashSet {
    public static void main(String[] args) {

        String s = "abcabcbb";

        int left = 0;
        int right = 0;
        int maxLength = 0;

        HashSet<Character> set = new HashSet<>();

        while (right < s.length()) {		

            char ch = s.charAt(right);		//c

            if (!set.contains(ch)) {
                set.add(ch);			//abc
                maxLength = Math.max(maxLength, right - left + 1);  	//1
                right++;
            } else {
                set.remove(s.charAt(left));
                left++;
            }
        }

        System.out.println("Longest Length = " + maxLength);
    }
}

