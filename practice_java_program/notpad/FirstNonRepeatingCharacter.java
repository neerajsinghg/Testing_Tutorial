import java.util.*;
public class FirstNonRepeatingCharacter{
	public static void main(String[] args){
		String input="swiss";
		HashMap<Character, Integer> hs=new HashMap<>();
		for(char ch:input.toCharArray()){
			hs.put(ch, hs.getOrDefault(ch, 0)+1);
		}
		for(Map.Entry<Character,Integer> entry:hs.entrySet()){
			if(entry.getValue()==1){
				System.out.println(entry.getKey());
				break;
			}
		}
	}	
}