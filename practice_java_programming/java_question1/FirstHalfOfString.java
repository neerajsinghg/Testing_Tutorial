package java_question1;

public class FirstHalfOfString {

	public static void main(String[] args) {
		String str = "This is my pen";
		char [] ch = str.toCharArray();
		String firstHalf = " ";
		int middile = str.length()/2;
		for(int i=0; i<=middile;i++) {
			firstHalf +=ch[i];
		}
		
		System.out.println(firstHalf);
	}

}
