public class SecondLargest{
	public static void main(String[] args){
		int[] numbers = {1,3,4,5,9,2,8};
		int largest=Integer.MIN_VALUE;
		int secondLargest = Integer.MIN_VALUE;
		for(int num:numbers){
			if(num>largest){
				secondLargest =largest;
				largest=num;
			}
			else if(num>secondLargest && num !=largest){
				secondLargest=num;
			}
		}
		System.out.println("largest = " +largest);
		System.out.println("second largest = "+secondLargest);
	}
}