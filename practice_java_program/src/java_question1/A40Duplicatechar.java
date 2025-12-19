package java_question1;

import java.util.HashMap;
import java.util.Map.Entry;

public class A40Duplicatechar {

	public static void main(String[] args) {
		
		String str = "Programmmming";
		char[] ch = str.toCharArray();
		
		HashMap<Character, Integer> hs = new HashMap<>();
		
		for(char ch1 : ch) {
			hs.put(ch1, hs.getOrDefault(ch1, 0)+1);
			//System.out.println(hs);
		}
		for(Entry<Character,Integer> entry : hs.entrySet()) {
			if (entry.getValue()>1) {
				System.out.println(entry.getKey()+" is = "+ entry.getValue());
			}
		}

	}

}
