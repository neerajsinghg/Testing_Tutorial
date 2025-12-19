package src.sortingAndsearchAlgoritham;

public class LinearSearch {

	public static void main(String[] args) {
		int [] arr = {6,3,9,2,1,2,3,4,5,6,7,8,9};
		int targate = 7;
		linearSearch(arr,targate);		
		}
	public static void linearSearch(int[] arr, int targate) {
		boolean found =false;
		for(int i=0; i<arr.length; i++) {
			if(arr[i]==targate) {
				System.out.println("Index of targate = "+i);
				found = true;
			}

	}
		if(!found) {
			System.out.println("element not found");
		}

	}
}