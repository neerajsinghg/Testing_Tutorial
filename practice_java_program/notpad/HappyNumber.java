public class HappyNumber{
	public static void main(String[] args){
		int num=19;
		
		int fast = num;
		int slow = num;
		while(true){
			slow=getSum(slow); //by 1 step
			fast = getSum(getSum(fast)); //2 step
			if(slow==fast){
				break;
			}
		}
		if (slow==1){
			System.out.println("this is happy num");
		}
		else{
			System.out.println("this is not a happy num");
		}	
	}
	public static int getSum(int num){
		int sum=0;
		while(num>0){
			int digit=num%10;
			sum += digit*digit;
			num=num/10;
		}
		return sum;
	}
}