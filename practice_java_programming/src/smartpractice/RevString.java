package src.smartpractice;

public class RevString {

	public static void main(String[] args) {
		String str = "My name is Hemant";
		String[] word = str.split(" ");
		
		for(int i=word.length-1; i>=0; i--) {
			System.out.print(word[i]+ " ");
		}

	}

}
