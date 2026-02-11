public class RightRotatebyK{
	public static void main(String[] args){
		int[] numbers = {1,2,3,4,5,6,7,8};   //o/p-{6,7,8,1,2,3,4,5}
		int k=3;
		int n=numbers.length;
		k=k%n;
		int[] temp = new int[n];
		
		//System.out.println(k);
		for(int i=0; i<n; i++){
			temp[(i+k)%n] = numbers[i];
		}
		for(int num:temp){
			System.out.print(num+" ");
		}
	}
}