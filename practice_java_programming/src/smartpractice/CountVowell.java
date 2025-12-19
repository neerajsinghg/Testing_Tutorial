package src.smartpractice;

public class CountVowell {

	public static void main(String[] args) {
		String str1 = "sOuthafrica";
		String str = str1.toLowerCase();
		int count =0;
		char [] ch = str.toCharArray();
		for(char ch1:ch) {
			if(ch1=='a'|| ch1=='e'||ch1=='i'|| ch1=='o'||ch1=='u'){
				count+=1;
			}
		}
		System.out.println(count);

	}

}
