import java.util.*;
public class logestSubstringWithoutRepeatingCharacter{
	public static void main(String[] args){
		String s = "abcabcbb";
		int left = 0;
		int maxLength = 0;
		int startIndex = 0;
		Set<Character> set = new HashSet<>();
		
		for(int right=0; right<s.length(); right++){ //bca
			while(set.contains(s.charAt(right))){
				set.remove(s.charAt(left));
				left++;
			}
			set.add(s.charAt(right));
			if((right-left+1)> maxLength){
				maxLength=right-left+1;
				startIndex= left;
			}
		}
		System.out.println(maxLength);	
		System.out.println("Substring: "+s.substring(startIndex, startIndex+maxLength));	
	}		
}