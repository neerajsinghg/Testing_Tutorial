package java_question1;

public class A53NoDivisibleBy23 {

	public static void main(String[] args) {
		int no = 250;
		for(int i=1; i<=no; i++) {
			if (i%2==0 && i%3==0) {
				System.out.print(i+" ");
			}
		}
		
	}

}
