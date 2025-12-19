package smartpractice;

public class RevChar {

	public static void main(String[] args) {
		String str = "Welcome to java";
		char[] ch = str.toCharArray();
		System.out.print("reverse char = ");
		for(int i =ch.length-1; i>=0; i--) {
			System.out.print(ch[i]);
		}

	}

}
