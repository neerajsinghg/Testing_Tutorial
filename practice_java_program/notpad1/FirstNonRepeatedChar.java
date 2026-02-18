import java.util.*;
public class FirstNonRepeatedChar{
	public static void main(String[] args){
		String s = "swiss"; // w
		char[] ch = s.toCharArray();
		Map<Character, Integer> hs=new LinkedHashMap<>();
		for(char chh:ch){
			hs.put(chh, hs.getOrDefault(chh,0)+1);
		}
		for(Map.Entry<Character, Integer> entry:hs.entrySet()){
			
		}
	}
}