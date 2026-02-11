import java.util.*;
public class SubArrayWithRequredSum{
	public static void main(String[] args){
		int[] numbers = {1,2,3,4,5,6,7,8};
		int targate = 8;
		
		HashSet<Integer> hs=new HashSet<>();
		for(int num:numbers){
			int complement=targate-num;
			if(hs.contains(complement)){
				System.out.println(targate +" = "+ num+" + "+complement);
				break;
			}
			else{
			hs.add(num);
			}
		}	
	}
}