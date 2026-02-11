import java.util.*;
public class CountFrequency{
	public static void main(String[] args){
		
		String name = "Neeraj Singh";
		HashMap<Character, Integer> hs= new HashMap<>();
		
		for(char ch : name.toCharArray()){
			if(ch==' '){
				continue;
			}
			else{
				hs.put(ch, hs.getOrDefault(ch, 0)+1);
			}
		}
		for(char ch:hs.keySet()){
			System.out.println(ch +" = " +hs.get(ch));
		}
	}
}