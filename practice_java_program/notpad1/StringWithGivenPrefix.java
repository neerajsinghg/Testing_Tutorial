//Check if string starts with a given prefix
public class StringWithGivenPrefix{
	public static void main(String[] args){
		String str="This is pen that those".toLowerCase();
		for(String word:str.split(" ")){
			if(word.contains("s")){
				System.out.println(true);
			}
		}
	}
}