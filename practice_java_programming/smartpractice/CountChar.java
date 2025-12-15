package smartpractice;
import java.util.Map;
import java.util.HashMap;
public class CountChar {

	public static void main(String[] args) {
		String str = "Test Automation";
		char[] ch = str.toCharArray();
		Map<Character, Integer> hs = new HashMap<>();
		for(char ch1:ch) {
			if(ch1 !=' ')
		{hs.put(ch1, hs.getOrDefault(ch1, 0)+1);
		}}
		System.out.println(hs);
	}

}
