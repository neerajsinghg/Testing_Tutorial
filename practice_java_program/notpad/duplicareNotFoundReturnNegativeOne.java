import java.util.*;
class duplicareNotFoundReturnNegativeOne{
	public static void main(String[] args){
		int[] num = {6,1,2,11,11,11,5,9,9,7,8};
		boolean duplicateindex =false;
		HashMap<Integer, Integer> hs = new HashMap<>();
		for(int no:num){
			hs.put(no, hs.getOrDefault(no,0)+1);
		}
		int maxduplivalue = 0;
		int maxduplickey=0;
		for(Map.Entry<Integer, Integer> entry:hs.entrySet()){
			if(entry.getValue()>maxduplivalue){
				maxduplivalue =entry.getValue();
				maxduplickey=entry.getKey();
				duplicateindex =true;
			}			
		}
		if(duplicateindex==false) {
			System.out.println("-1");
		} 
		else{
			System.out.println(maxduplickey+" - "+maxduplivalue );
		}
		
	}
}