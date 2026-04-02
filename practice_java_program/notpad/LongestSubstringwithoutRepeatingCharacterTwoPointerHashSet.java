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



import java.util.*;

public class Main {
    public static void main(String[] args) {

        String s = "abcabcbb";

        Set<Character> set = new HashSet<>();
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {  

            while (set.contains(s.charAt(right))) {   
                set.remove(s.charAt(left));   
                left++;
            }

            set.add(s.charAt(right));           
            maxLen = Math.max(maxLen, right - left + 1);
        }

        System.out.println("Longest substring length: " + maxLen);
    }
}