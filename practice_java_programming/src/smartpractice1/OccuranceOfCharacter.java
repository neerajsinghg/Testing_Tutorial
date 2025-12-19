package src.smartpractice1;

import java.util.HashMap;
import java.util.Map;

public class OccuranceOfCharacter {

	public static void main(String[] args) {
		String name = "Neeraj";
		char ch [] = name.toCharArray();
		HashMap<Character, Integer> hs = new HashMap<>();
		
		for(char ch1 : ch) {
			hs.put(ch1, hs.getOrDefault(ch1, 0)+1);
		}
		System.out.println(hs);
		
		char minchar =  ' ';
		char maxchar =  ' ';
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		
		for(Map.Entry<Character, Integer> entry: hs.entrySet()) {
			if(entry.getValue()>max) {
				max = entry.getValue();
				maxchar = entry.getKey();
			}
			if(entry.getValue()<min) {
				min = entry.getValue();
				minchar = entry.getKey();
				
			}
		}
		System.out.println("max char and value " +maxchar +" =" + max);
		System.out.println("min char and value "+minchar +" ="+ min);
		
	}

}
