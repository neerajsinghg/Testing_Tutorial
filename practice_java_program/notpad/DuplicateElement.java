import java.util.*;
public class DuplicateElement{
	public static void main(String[] args){
		String s = "Deepaak singh";
		char[] ch = s.toCharArray();
		HashMap<Character, Integer> hs = new HashMap<>();
		for(char chh:ch){
			hs.put(chh, hs.getOrDefault(chh, 0)+1);
		}
		//for(char chhh:hs.keySet()){
		//	System.out.println(chhh);
		//	if(hs.get(chhh)>=2){
		//		System.out.println(chhh+" = "+hs.get(chhh));
		//	}
		//}
		
		for(Map.Entry<Character, Integer> entry:hs.entrySet()){
			if(entry.getValue()>=2){
				System.out.println(entry.getKey()+" = "+entry.getValue());
			}
		}
	}
}