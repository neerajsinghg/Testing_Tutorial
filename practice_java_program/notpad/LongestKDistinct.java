//Longest Substring with At Most K Distinct Characters
import java.util.*;
public class LongestKDistinct{
    public static void main(String[] args) {
        String s = "eceba";
        int k = 2;
        HashMap<Character, Integer> map = new HashMap<>();

        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);
            map.put(ch, map.getOrDefault(ch, 0) + 1);

            while (map.size() > k) {

                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar) - 1);

                if (map.get(leftChar) == 0) {
                    map.remove(leftChar);
                }
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        System.out.println("Longest Length: " + maxLen);
    }
}
