package smartpractice1;

public class Cap {
	public static void main(String[] args) {
		
		String str= "how are you";
		StringBuilder sb = new StringBuilder();
		String[] word = str.split(" ");
		for(String word1 : word) {
			String cap = word1.substring(0,1).toUpperCase()+word1.substring(1).toLowerCase();
			sb.append(cap+" ");
		}
		System.out.println(sb.toString().trim());
	}
}
