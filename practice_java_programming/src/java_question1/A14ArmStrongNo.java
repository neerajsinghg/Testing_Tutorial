package java_question1;

public class A14ArmStrongNo {

	public static void main(String[] args) {
		int no=153;
		int ono = no;
		int result =0;
		while(no>0) {
			int digit = no%10;
			result += digit*digit*digit;
			no=no/10;
		}
		if (ono==result) {
			System.out.println("this is armstrong no");
		}
		else {
			System.out.println("this is not armstrog no");
		}

	}

}
