package arraylist;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayListToArray {
		public static void main(String[] args) {
			
			List<Integer>  ls = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9));
			
			
			System.out.println(ls);
			int [] arr = new int[ls.size()];
			for(int i=0; i<ls.size(); i++) {
				arr[i]=ls.get(i);
			}
			System.out.println(Arrays.toString(arr));
		}
}
