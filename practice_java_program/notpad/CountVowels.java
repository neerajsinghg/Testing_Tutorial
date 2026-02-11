public class CountVowels{
	public static void main(String[] args){
		
		String s = "United State of America";
		int count = 0;
		char[] arr = s.toCharArray();
		StringBuilder sb = new StringBuilder();
		for(char ch : arr){
		if(isVowel(ch)){
			sb.append("X");
			count++;
		}
		else{
			sb.append(ch);
		}

		}
		System.out.println(sb.toString());
		System.out.println("vowel count = "+count);

	}
	public static boolean isVowel(char ch){
		ch=Character.toLowerCase(ch);
		return ch=='a'|| ch=='e'|| ch=='i'|| ch=='o' || ch=='u';
	}
}