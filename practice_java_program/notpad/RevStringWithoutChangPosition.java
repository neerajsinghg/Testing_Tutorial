public class RevStringWithoutChangPosition{
	public static void main(String[] args){
		String s = "this is my pen";  //o/p- nep ym si siht
		char[] ch=s.toCharArray();
		int left = 0;
		int right = ch.length-1;
		while(left<right){
			char temp=ch[left];
			ch[left]=ch[right];
			ch[right]=temp;

			left++;
			right--;
		}
		System.out.println(new String(ch));
	}
}