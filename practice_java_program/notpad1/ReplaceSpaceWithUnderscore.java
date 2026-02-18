public class ReplaceSpaceWithUnderscore{
	public static void main(String[] args){
		String str="this is my pen";
		char[] ch=str.toCharArray();
		for(int i=0; i<ch.length; i++){
			if(ch[i]==' '){
				ch[i]='_';
			}
		}
		System.out.println(new String(ch));
	}
}