public class ShiftZeroRightArray{
	public static void main(String[] args){
		int [] numbers = {4,0,3,0,5,0,6,0};
		int index=0;
		for(int i=0; i<numbers.length; i++){
			if(numbers[i] !=0){
				numbers[index]=numbers[i];
				index++;
			}
		}
		while(index<numbers.length){
			numbers[index]=0;
			index++;
		}
		for(int num:numbers){
			System.out.print(num+", ");
		}
	}
}