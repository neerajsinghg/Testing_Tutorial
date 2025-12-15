package java_question1;

public class A66InsertWordInMiddile {

	public static void main(String[] args) {
		String str = "this is new pen";
		String insert = "my";
		int middile= str.length()/2;
		String result = str.substring(0,middile)+" "+ insert+ str.substring(middile);
		System.out.println(result);

	}

}
