package java_question1;

public class SecondLastWordInSentence {

	public static void main(String[] args) {
		
		String str = "this is my new parker pen";
		String[] str1 = str.split(" ");
		String str2= str1[str1.length-2];
		System.out.println(str2);

	}

}
