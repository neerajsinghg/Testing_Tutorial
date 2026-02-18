import java.util.*;
public class StringCompressionHashMap{
	public static void main(String[] args){
		String s= "aabcccdddd";
		char[] ch= s.toCharArray();
		HashMap<Character, Integer> hs=new HashMap<>();
		for(char c:ch){
			hs.put(c, hs.getOrDefault(c,0)+1);
		}
		//for(char chh:hs.keySet()){
		//	System.out.print(chh+""+hs.get(chh));
		//}
		for(Map.Entry<Character, Integer> entry:hs.entrySet()){
			System.out.print(entry.getKey()+""+entry.getValue());
		}
	}
}