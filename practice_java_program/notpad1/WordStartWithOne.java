//Count how many numbers in array start with 1
public class WordStartWithOne{
	public static void main(String[] args){
		int[] numbers = {11,14,143,453,641,1994};
		for(int num:numbers){
			if(String.valueOf(num).startsWith("1")){
				System.out.println(num);
			}
		}
	}
}