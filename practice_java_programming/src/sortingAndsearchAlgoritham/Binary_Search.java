package src.sortingAndsearchAlgoritham;

import java.util.Arrays;

public class Binary_Search {

	public static void main(String[] args) {
		
		int[] arr = {6,3,9,2,1,2,3,4,5,6,7,8,9};
		Arrays.sort(arr);
		int targate = 7;
		int left=0;
		int right = arr.length-1;
		
		
		while(left<=right) {
			int mid = (left+right)/2;
		if(arr[mid] == targate) {
			System.out.println("targate is found at index = "+mid);
			return;
		}
		else if(arr[mid]<targate) {
			left = mid+1;
		}
		else if(arr[mid]>targate) {
			right = mid-1;
		}

	}
		System.out.println("Element not found");

}
}
