import java.util.*;
public class DupliandNonDuplicateElements{
	public static void main(String[] args){
		int[] numbers = {1,2,3,4,5,5,6,6,2};
		HashSet<Integer> unique = new HashSet<>();
		HashSet<Integer> duplicate = new HashSet<>();
		for(int num:numbers){
			if(unique.contains(num)){
				duplicate.add(num);
			}
			else{
				unique.add(num);
			}	
		}
		System.out.println("unique element = "+unique);
		System.out.println("duplicate element = "+duplicate);
	}
}