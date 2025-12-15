package java_question1;

public class A13PalindromNo {

	public static void main(String[] args) {
		
		int no =12321;
		int ono =no;
		int rev = 0;
		while(no !=0) {
			int digit = no%10;
			rev = rev*10+digit;
			no=no/10;
		}
		System.out.println(rev);
		System.out.println(no);
		if(ono==rev) {
			System.out.println("This is a pelindrom no ");
		}
		else {
			System.out.println("this is not a pelindrom no ");
		}

	}

}
