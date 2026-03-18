//387. First Unique Character in a String
//Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
//Example 1:
//Input: s = "leetcode"
//Output: 0
//Explanation:
//The character 'l' at index 0 is the first character that does not occur at any other index.
//Example 2:
//Input: s = "loveleetcode"
//Output: 2
//Example 3:
//Input: s = "aabb"
//Output: -1

import java.util.*;
class FirstUniqueCharacterIndexInString{
    public static void main(String[] args){
	String s= "lovecode";
	System.out.println(firstUniqChar(s));
	System.out.println(firstUniqCharacter(s));
    }
    public static int firstUniqChar(String s) {
        LinkedHashMap<Character, Integer> hs = new LinkedHashMap<>();
        for(char ch:s.toCharArray()){
            hs.put(ch, hs.getOrDefault(ch,0)+1);
        }
        for(Map.Entry<Character, Integer> entry:hs.entrySet()){
            if(entry.getValue()==1){
                return s.indexOf(entry.getKey());
            }
        }
        return -1;
    }
	
    public static int firstUniqCharacter(String s) {
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++){
            count[s.charAt(i) - 'a']++;
        }
        for(int i = 0; i < s.length(); i++){
            if(count[s.charAt(i) - 'a'] == 1){
                return i;
            }
        }
        return -1;
    }
}