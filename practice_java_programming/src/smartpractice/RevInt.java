package src.smartpractice;

public class RevInt {

	public static void main(String[] args) {
		/*
		 int no = 256;
		String num = String.valueOf(no);
		char [] ch = num.toCharArray();
		StringBuilder sb = new StringBuilder();
		for (char ch1:ch) {
			sb.append(ch1);
		}
		
		sb.reverse();
		String str= sb.toString();
		int num1 = Integer.parseInt(str);
		Object obj = num1;
		System.out.println((num1));
		System.out.println(obj.getClass().getSimpleName());
		 */
		int no = 25623478;
		int rev=0;
		while(no !=0) {
			int digit = no%10;
			rev = digit +rev*10;
			no = no/10;
		}
		System.out.println(rev);
	}

}
