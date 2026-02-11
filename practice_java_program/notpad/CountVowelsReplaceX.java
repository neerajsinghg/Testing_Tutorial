import java.util.*;
public class CountVowelsReplaceX{
	public static void main(String[] args){
		String s= "united state of america";
		char[] ch = s.toCharArray();
		int count = 0;
		StringBuilder sb = new StringBuilder();
		for(char chh:ch){
			if(isVowel(chh)){
				count++;
				sb.append('X');
			}
			else{
				sb.append(chh);
			}
		}
		System.out.println(sb);
		System.out.println("total number of vowels = "+count);
	}
	public static boolean isVowel(char chh){
		return 'a'==chh || 'e'==chh || 'i'==chh|| 'o'==chh || 'u'==chh;

	}
}