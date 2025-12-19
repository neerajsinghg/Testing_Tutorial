package src.smartpractice1;

import java.util.ArrayList;
import java.util.List;

public class LeaderElement {

	public static void main(String[] args) {
		int [] no = {56,10,3,4,55,6,1,2,7,9,8};
		List<Integer> l = new ArrayList<>();
		
		int last = no[no.length-1];
		l.add(last);
		
		for(int i=no.length-2; i>=0; i--) {
			if(no[i]>last) {
				last = no[i];
				l.add(last);
						
			}
		}
		System.out.println(l);

	}

}
