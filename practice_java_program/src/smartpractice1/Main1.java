package smartpractice1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main1 {

	public static void main(String[] args) {
		
		        List<Object> objList = Arrays.asList(1, 10, 2, 5, 'a', 'z', 'c', 'f', 'h');
		        System.out.println(objList.getClass());

		        List<Integer> intList = new ArrayList<>();
		        List<Character> charList = new ArrayList<>();

		        for (Object obj : objList) {
		        	
		            if (obj.getClass().equals(Integer.class)) {
		                intList.add((Integer) obj);
		            } else if (obj.getClass().equals(Character.class)) {
		                charList.add((Character) obj);
		            }
		        }

		        Collections.sort(intList);
		        Collections.sort(charList);

		        List<Object> finalList = new ArrayList<>();
		        finalList.addAll(charList);
		        finalList.addAll(intList);

		        System.out.println(finalList);  // Output: [a, c, f, h, z, 1, 2, 5, 10]
		    }
}
