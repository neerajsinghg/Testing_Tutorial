package java_question1;

public class A131PalindromNo {

	public static void main(String[] args) {
		
		int no =12321;
		int ono =no;
		int rev = 0;
		
		StringBuilder sb = new StringBuilder();
		String str = String.valueOf(no);
		char[] ch = str.toCharArray();
		for(int i=ch.length-1; i>=0; i--) {
			sb.append(ch[i]);	
		}
		
		rev = Integer.parseInt(sb.toString());
		System.out.println(ono);
		System.out.println(rev);	
		
		if(ono==rev) {
			System.out.println("This is a pelindrom no ");
		}
		else {
			System.out.println("this is not a pelindrom no ");
		}

	}

}
