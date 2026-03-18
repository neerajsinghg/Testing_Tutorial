import java.util.*;
public class MapSortByValue{
	public static void main(String[] args){
		String str = "this is my pen and my pen";
		char[] chh = str.toCharArray();
		HashMap<Character, Integer> hs = new HashMap<>();
		for(char ch:chh){
			hs.put(ch, hs.getOrDefault(ch,0)+1);
		}
		ArrayList<Map.Entry<Character,Integer>> list=new ArrayList<>(hs.entrySet());
		Collections.sort(list, (a,b) -> b.getValue().compareTo(a.getValue()));
		
		for(Map.Entry<Character,Integer> entry:list){
			System.out.println(entry.getKey()+" - "+entry.getValue());
		}
	}
}