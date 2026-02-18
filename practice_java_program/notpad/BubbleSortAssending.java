//Bubble Sort - Repeatedly swap adjacent elements if they are in wrong order.
//Time Complexity: Worst: O(n²)       Best: O(n) (optimized)

public class BubbleSortAssending{
	public static void main(String[] args){
		int[] numbers = {4,3,1,5,6,2,9};
		
		for(int i=0; i<numbers.length; i++){
			for(int j=i+1; j<numbers.length; j++){
				if(numbers[i]>numbers[j]){
					int temp=numbers[i];
					numbers[i]=numbers[j];
					numbers[j]=temp;
				}
			}
		}
		for(int nums:numbers){
			System.out.print(nums+" ");
		}
	}
}