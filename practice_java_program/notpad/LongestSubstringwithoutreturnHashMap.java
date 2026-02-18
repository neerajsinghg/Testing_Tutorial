import java.util.*;

public class LongestSubstringwithoutreturnHashMap{
    public static void main(String[] args) {

        String s = "abcabcbb";

        HashMap<Character, Integer> map = new HashMap<>();

        int left = 0;
        int maxLength = 0;
        int startIndex = 0;

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            if (map.containsKey(ch)) {
                left = Math.max(left, map.get(ch) + 1);
            }

            map.put(ch, right);

            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
                startIndex = left;
            }
        }

        String result = s.substring(startIndex, startIndex + maxLength);

        System.out.println("Longest Substring = " + result);
        System.out.println("Length = " + maxLength);
    }
}
