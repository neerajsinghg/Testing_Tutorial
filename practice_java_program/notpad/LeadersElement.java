public class LeadersElement{
	public static void main(String[] args){
		int[] numbers = {16, 17, 4,3,5,2}; //Leaders element 17, 5, 2
		int maxFromRight = numbers[numbers.length-1];
		System.out.print("Leaders Elements = "+  maxFromRight);
		for(int i=numbers.length-2; i>=0; i--){
			if(numbers[i]>maxFromRight){
				maxFromRight=numbers[i];
				System.out.print(", "+maxFromRight);
			}
		}
	}
}