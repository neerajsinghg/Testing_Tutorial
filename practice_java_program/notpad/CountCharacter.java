public class CountCharacter{
	public static void main(String[] args){
		String s = "this is 443 my e45 pen";
		int count = 0;
		//Object[] arr = new Object[s.length()];
		//for(int i=0; i<s.length(); i++){
		//	arr[i]=s.charAt(i);
		//}
		//for(Object o:arr){
		//	char ch = (Character) o;
		//	if(Character.isLetter(ch) || Character.isWhitespace(ch)){
		//		System.out.print(ch);
		//	}
		//}
		for(int i=0; i<s.length(); i++){
			char ch=s.charAt(i);
			if(Character.isLetter(ch)){
				count++;
			}
		}
		System.out.println("total number of letter in sentence = "+count);
	}
}