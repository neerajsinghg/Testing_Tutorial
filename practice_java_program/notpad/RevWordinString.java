import java.util.Arrays;
public class RevWordinString{
	public static void main(String[] args){
		String s = "this is my pen";
		String[] arr = s.split(" ");
		System.out.println(Arrays.toString(arr));
		for(String str:arr){
			char[] ch = str.toCharArray();
			int left= 0;
			int right = ch.length-1;
			while(left<right){
				char temp=ch[left];
				ch[left]=ch[right];
				ch[right]=temp;
				left++;
				right--;
			}
			System.out.print(new String(ch)+", ");
		}
	}
}