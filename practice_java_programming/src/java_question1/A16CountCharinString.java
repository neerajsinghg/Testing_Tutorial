package java_question1;

public class A16CountCharinString {

	public static void main(String[] args) {
		String str = "This is my pen";
		int count =0;
		//System.out.println(str.length());
		for(char ch : str.toCharArray()) {
			
			if(ch != ' ' ) {
				count +=1;
			}
			
		}
		System.out.println(count);
		

	}

}
