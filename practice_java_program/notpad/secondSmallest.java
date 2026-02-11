public class secondSmallest{
	public static void main(String[] args){
		int[] numbers = {3,6,7,1,4,2};
		int smallest = Integer.MAX_VALUE;
		int secondSmallest = Integer.MAX_VALUE;
		for(int num:numbers){					//smallest=1    secondsmallest=3
			if(num<smallest){
				secondSmallest=smallest;
				smallest=num;
			}
			else if(num<secondSmallest && num != smallest){     //secondsmallest=2
				secondSmallest=num;
			}
		}
		System.out.println("smallest = "+smallest);
		System.out.println("second smallest = "+secondSmallest);
	}
}