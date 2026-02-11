public class CapitaliseFirstLetterOfEachWord{
	public static void main(String[] args){
	 	String s = "this is my pen";
		String[] str = s.split(" ");
		StringBuilder sb=new StringBuilder();
		for(String word:str){
			sb.append(Character.toUpperCase(word.charAt(0))+word.substring(1)+" ");
		}
		System.out.println(sb.toString().trim());
		
	}
}