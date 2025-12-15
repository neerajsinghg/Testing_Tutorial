package java_question1;

public class A29CountWordInString {

	public static void main(String[] args) {
		
		String str = "This is my pen";
		String[] str1= str.split(" ");
		int count =0;
		for(String str2 : str1) {
			count+=1;
			System.out.println(str2);
		}
		System.out.println(count);
		

	}

}
