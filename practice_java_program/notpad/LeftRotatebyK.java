public class LeftRotatebyK{
	public static void main(String[] args){
		int[] numbers = {1,2,3,4,5,6,7,8}; //o/p={4,5,6,7,8,1,2,3}
		int k=3;
		int n=numbers.length;
		 k=k%n;
		int[] temp = new int[n];
		
		for(int i=0; i<n; i++){
			temp[i]=numbers[(i+k)%n];
		}
		for(int num:temp){
			System.out.print(num+" ");
		}
	}
}