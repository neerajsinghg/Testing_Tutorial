package src.smartpractice;
import java.util.*;
public class LeaderElement {

	public static void main(String[] args) {
		
		int [] no = {5,7,6,1,3,2} ;
		List<Integer> leaders = new ArrayList<>();
		
		int maxFromRight = no[no.length-1];
		 leaders.add(maxFromRight);
		 
		for(int i=no.length-2; i>=0; i--) {
			if(no[i]>maxFromRight) {
				maxFromRight=no[i];
				leaders.add(maxFromRight);
			}
			
		}
		System.out.println(leaders);

	}

}
