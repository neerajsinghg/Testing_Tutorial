public class StringCompress{
	public static void main(String[] args){
		String str = "aabccddd"; //a2b1c2d3
		StringBuilder sb=new StringBuilder();
		int count=1;
		for(int i=1; i<str.length(); i++){
			if(str.charAt(i)==str.charAt(i-1)){//a b c
				count++;//a-2  c-2
			}
			else{
				sb.append(str.charAt(i-1)).append(count);//a2b1c2
				count=1;
			}
		}
		sb.append(str.charAt(str.length()-1)).append(count);
		System.out.println(sb);
	}
}