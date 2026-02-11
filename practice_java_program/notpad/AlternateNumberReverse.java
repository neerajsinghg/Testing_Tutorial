import java.util.Arrays;
public class AlternateNumberReverse{
	public static void main(String[] args){
		int[] numbers = {1,2,3,4,5,6,7};
		int left=0;
		int right=numbers.length-1;
		while(left<right){
			int temp = numbers[left];
			numbers[left]=numbers[right];
			numbers[right]=temp;
			left+=2;
			right-=2;
		}
		System.out.println(Arrays.toString(numbers));
	}
}