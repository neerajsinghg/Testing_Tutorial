package arraylist;

import java.util.ArrayList;
import java.util.List;

public class ArrayList1 {

	public static void main(String[] args) {
		
		List<Integer> ls = new ArrayList<>();
		ls.add(1);
		ls.add(2);
		ls.add(3);
		ls.add(4);
		ls.add(5);
		ls.add(6);  
		System.out.println(ls);
		for(int i=0; i<=ls.size()-1; i++) {
			//System.out.print(ls.get(i)+" "); 
			Integer value = ls.get(i);
			System.out.println(i+"= " +value);
		}
		

	}

}
