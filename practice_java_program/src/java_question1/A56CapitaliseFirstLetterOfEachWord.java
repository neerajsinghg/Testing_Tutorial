package java_question1;

public class A56CapitaliseFirstLetterOfEachWord {

	public static void main(String[] args) {
		
		String str = "this is a pen";
		String[]str1= str.split(" ");
		StringBuilder sb = new StringBuilder();
		for(String word:str1) {
			String cap = word.substring(0,1).toUpperCase()+word.substring(1).toLowerCase();
			sb.append(cap).append(" ");
			
		}
		System.out.println(sb.toString().trim());

	}

}
