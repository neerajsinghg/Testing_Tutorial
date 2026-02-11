public class FirstandLastOccurance{
	public static void main(String[] args){
		String input = "Hello World";
        	char target = 'o'; 
		int firstindex=-1;
		int lastindex=-1;
		// at first index
		for(int i=0; i<input.length(); i++){
			if(input.charAt(i)==target){
				firstindex=i;
				break;
			}
		}
		// at last index
		for(int i=input.length()-1; i>=0; i--){
			if(input.charAt(i)==target){
				lastindex=i;
				break;
			}
		}
		if(firstindex<0){
			System.out.println("Character "+target+"is not present in string");
		}
		else{
			System.out.println("first index for "+target+" = " +firstindex);
			System.out.println("last index for "+target+" = " +lastindex);
		}
	}
}