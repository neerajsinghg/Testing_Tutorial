package dsa;

public class RevArray {
	public static void reverseArray(int[]arr) {
		int start = 0;
		int end = arr.length-1;
		while(start<=end) {
			int temp =arr[start];
			arr[start]=arr[end];
			arr[end] = temp;
			start++;
			end--;
		}
		for(int num: arr) {
			System.out.print(num+" ");
		}
	}
	public static void main(String[] args) {
		int[] arr = new int[]{21,43,54,32,65};
		reverseArray(arr);

	}

}
