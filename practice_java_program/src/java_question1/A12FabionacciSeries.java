package java_question1;

public class A12FabionacciSeries {

	public static void main(String[] args) {
		
		int n=10;
		int first =0, second = 1;
		System.out.println("Fabbionacci series of "+n+" terms");
		for(int i=1; i<=n; i++) {
			System.out.print(first + " ");
			int next = first+second;
			first=second;
			second = next;
			
		}

	}

}
