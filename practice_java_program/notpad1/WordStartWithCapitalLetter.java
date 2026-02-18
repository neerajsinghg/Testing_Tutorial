//Filter words starting with capital letter
public class WordStartWithCapitalLetter{
	public static void main(String[] args){
		String str = "this Is May Pen";
		String[] word=str.split(" ");

		for(String words:word){
			if(Character.isUpperCase(words.charAt(0))){
				System.out.println(words);
			}
		}
	}
}