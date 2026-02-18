//Remove all digits from string
import java.util.*;
public class RemoveDigitsFromString{
	public static void main(String[] args){
		String str = "Java123 Programming456";
		char[] arr= str.toCharArray();
		StringBuilder sb=new StringBuilder();
		for(char ch:arr){
			if(!Character.isDigit(ch)){
				sb.append(ch);
			}
		}
		System.out.print(sb);
	}	
}