public class StarPattern2{
	public static void main(String[] args){
		for(int i=1; i<=5; i++){	//1
			for(int j=5; j>=i; j--){ //5
				System.out.print("* ");
			}
			System.out.println();
		}
	}
}
"""
* * * * *
* * * *
* * *
* *
*
"""