package dsa;

public class KthMaxMinValueArray {
	public static void kthMaxMinElements(int[] no, int a) {
		
		int n=no.length;
		for(int i=0; i<n; i++) {
			for(int j=0;j<n-i-1;j++) {
				if(no[j]>no[j+1]) {
					int temp = no[j];
					no[j]=no[j+1];
					no[j+1]=temp;
				}
			}
		}
		
		for(int num:no) {
			System.out.print(num+" ");
		}
		
		System.out.println();
		//find kth max and min element
		System.out.println(a+ " minimum element in array = "+no[a-1]);
		System.out.println(a+ " maxmium element in array = "+no[no.length-a]);
		
	}

	public static void main(String[] args) {
		int[] no = {0,1,2,0,1,2,0,1,2,3,3};
		int a=2;
		kthMaxMinElements(no,a);

	}

}
