package java_question1;

public class A38SumOfFirst100N {

	public static void main(String[] args) {
		int n = 100;
		//int sum = n*(n+1)/2;
		//System.out.println(sum);
		int sum=0;
		for(int i=1; i<=n; i++) {
			sum+=i;
		}
		System.out.println(sum);
	}

}
