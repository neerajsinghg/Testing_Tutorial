import java.util.*;
public class CountFreqMaxMin{
	public static void main(String[] args){
		String name = "Neeraj Singh";
		HashMap<Character, Integer> hs = new HashMap<>();
		for(char ch:name.toCharArray()){
			if(ch==' '){
				continue;
			}
			else{
				hs.put(ch, hs.getOrDefault(ch, 0)+1);
			}
		}
		//for(Map.Entry<Character, Integer> entry: hs.entrySet()){
		//	System.out.println(entry.getKey()+" = "+entry.getValue());
		//}
		char maxchar = '\0';
		int maxvalue = 0;
		for(Map.Entry<Character, Integer> entry: hs.entrySet()){
			if(entry.getValue()>maxvalue){
				maxvalue=entry.getValue();
				maxchar=entry.getKey();
			}
		}
		System.out.println("max Occurance char "+maxchar+ " = "+ maxvalue);

		char minchar = '\0';
		int minvalue= Integer.MAX_VALUE;
		for(Map.Entry<Character, Integer> entry: hs.entrySet()){
			if(entry.getValue()<minvalue){
				minvalue=entry.getValue();
				minchar=entry.getKey();
			}
		}
		System.out.println("min Occurance char "+minchar+ " = "+ minvalue);
	}

}