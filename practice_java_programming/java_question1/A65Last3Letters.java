package java_question1;

public class A65Last3Letters {

	public static void main(String[] args) {
		String str = "this is my pencil";
		char[] ch = str.toCharArray();
		for(int i =ch.length-3; i<=ch.length-1; i++){
			System.out.print(ch[i]);
		}
	}

}
