public class ShiftZeroRight{
	public static void main(String[] args){
		int numbers = 804030;
		StringBuilder sb = new StringBuilder();
		int countzero=0;
		while(numbers!=0){
			int digit=numbers%10;
			if(digit==0){
				countzero++;
			}
			else{
				sb.append(digit);
			}
			numbers=numbers/10;
			sb.reverse();
		}
		for(int i=0;i<countzero;i++){
			sb.append('0');
		}
		System.out.println(sb);
	}
}