//1408. String Matching in an Array
//Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.
//Example 1:
//Input: words = ["mass","as","hero","superhero"]
//Output: ["as","hero"]
//Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
//["hero","as"] is also a valid answer.
//Example 2:
//Input: words = ["leetcode","et","code"]
//Output: ["et","code"]
//Explanation: "et", "code" are substring of "leetcode".
//Example 3:
//Input: words = ["blue","green","bu"]
//Output: []
//Explanation: No string of words is substring of another string

import java.util.*;
class StringMatchingArray{
    public static void main(String[] args){
	String[] words = {"mass","as","hero","superhero"};
	System.out.println(stringMatching(words));
    }
    public static List<String> stringMatching(String[] words) {
        List<String> result = new ArrayList<>();
        int n = words.length;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(i != j && words[j].contains(words[i])) {
                    result.add(words[i]);
                    break;
                }
            }
        }
        return result;
    }
}