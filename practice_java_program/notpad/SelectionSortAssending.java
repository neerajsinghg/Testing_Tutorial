//Selection Sort - Find minimum element and place it at correct position.
//Time Complexity: O(n²) (all cases)

public class SelectionSortAssending{
	public static void main(String[] args){
		int[] numbers = {4,3,1,5,6,2,9};

		for(int i=0; i<numbers.length-1; i++){
			int minindex=i;//4
			for(int j=i+1; j<numbers.length; j++){
				if (numbers[j]<numbers[minindex]){
					minindex=j;
				}
			}
			int temp=numbers[i];
			numbers[i]=numbers[minindex];
			numbers[minindex]=temp;
		}
		for(int nums:numbers){
			System.out.print(nums+" ");
		}
	}
}