import java.util.*;
public class BothStringAngrambyHashmap{
	public static void main(String[] args){
		String input1 = "listen";
		String input2 = "silent";
		if(input1.length()!=input2.length()){
			System.out.println("Strings are not anagram");
			return;
		}
		HashMap<Character, Integer> hs = new HashMap<>();
		for(char ch:input1.toCharArray()){
			hs.put(ch, hs.getOrDefault(ch,0)+1);
		}
		for(char ch:input2.toCharArray()){
			if(!hs.containsKey(ch)){
				System.out.println("not anagram");
				return;
			}
			hs.put(ch, hs.get(ch)-1);
			if(hs.get(ch)==0){
				hs.remove(ch);
			}
		}
		if(hs.isEmpty()==true){
			System.out.println("anagram");
		}
		else{
			System.out.println("not anagram");
		}
	}
}