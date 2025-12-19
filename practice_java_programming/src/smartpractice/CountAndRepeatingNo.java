package src.smartpractice;
import java.util.HashMap;
import java.util.Map;
public class CountAndRepeatingNo {

	public static void main(String[] args) {
		int[] no={1, 1, 1, 2, 3, 3};
		Map<Integer, Integer> hs = new HashMap<>();
		for(int num :no) {
			hs.put(num, hs.getOrDefault(num, 0)+1);
		}
		//System.out.println(hs);
		
		for(Map.Entry<Integer, Integer> entry:hs.entrySet()) {
			if(entry.getValue() >1) {
				System.out.println(entry.getKey()+ "=" +entry.getValue() );
			}
		}

	}

}
