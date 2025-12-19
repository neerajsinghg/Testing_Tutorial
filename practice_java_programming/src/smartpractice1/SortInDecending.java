package src.smartpractice1; 

public class SortInDecending {

	public static void main(String[] args) {
		/*
		 * Integer [] no = {1,0,1,0,1,0,1,0,1,0,1};
		 * Arrays.sort(no, Collections.reverseOrder());
		System.out.println(Arrays.toString(no));
		 */
		 String str = "10101010101010101";
		 char [] ch = str.toCharArray();
		 StringBuilder sb = new StringBuilder();
		 StringBuilder sb1 = new StringBuilder();
		 
		 for(int i=0; i<=ch.length-1; i++) {
			 if(ch[i]=='1') {
				 sb.append(ch[i]);
			 }
			 else {
				 sb1.append(ch[i]);
			 }
		 }
		 
		 System.out.println(sb.toString()+sb1.toString());

	}

}
