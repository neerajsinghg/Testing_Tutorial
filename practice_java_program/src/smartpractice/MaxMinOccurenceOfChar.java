package smartpractice;

import java.util.HashMap;
import java.util.Map;

public class MaxMinOccurenceOfChar {

	public static void main(String[] args) {
		String str = "Test Automation";
		char[] ch = str.toCharArray();
		Map<Character, Integer> hs = new HashMap<>();
		for(char ch1:ch) {
			if(ch1 !=' ')
		{hs.put(ch1, hs.getOrDefault(ch1, 0)+1);
		}}
		System.out.println(hs);
		
		char minChar = ' ';
		char maxChar = ' ';
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;

		for (Map.Entry<Character, Integer> entry : hs.entrySet()) {
		    if (entry.getValue() > max) {
		        max = entry.getValue();
		        maxChar = entry.getKey();
		    }
		    if (entry.getValue() < min) {
		        min = entry.getValue(); 
		        minChar = entry.getKey(); 
		    }
		}

		System.out.println("\nMax occurring character: " + maxChar + " with count " + max);
		System.out.println("Min occurring character: " + minChar + " with count " + min);


	}

}
