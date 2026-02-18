public class RotateArray{
	public static void reverse(int[] arr, int left, int right){
		while(left<right){
			int temp=arr[left];
			arr[left]=arr[right];
			arr[right]=temp;
			left++;
			right--;
		}
	}	
	public static void main(String[] args){
		int[] arr = {1,2,3,4,5};
		int k=2;
		int n=arr.length;

		k=k%n;

		reverse(arr, 0, n - 1);
        	reverse(arr, 0, k - 1);
        	reverse(arr, k, n - 1);

		for(int num:arr){
			System.out.print(num+" ");
		}
	}
}