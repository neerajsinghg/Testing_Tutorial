import java.util.*;
public class TwoStringAnagram{
	public static void main(String[] args){
		String input1 = "listen";
		String input2 = "silent";
		if(input1.length() != input2.length()){
			System.out.println("both string are not anagram");
			return;
		}
		
		char[] ch1 = input1.toCharArray();
		char[] ch2 = input2.toCharArray();
		Arrays.sort(ch1);
		Arrays.sort(ch2);
		if(Arrays.equals(ch1,ch2)){
			System.out.println("both string are anagram");
		}
		else{
			System.out.println("both string are not anagram");
		}
	}
}