//557. Reverse Words in a String III
//Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
//Example 1:
//Input: s = "Let's take LeetCode contest"
//Output: "s'teL ekat edoCteeL tsetnoc"
//Example 2:
//Input: s = "Mr Ding"
//Output: "rM gniD"

class revWord{
    public static void main(String[] args){
	String s = "leet code";
	System.out.println(reverseWords(s));	
}
    public static String reverseWords(String s) {
        String[] words=s.split(" ");
        StringBuilder sb = new StringBuilder();
        for(String word:words){
            char[] ch = word.toCharArray();
            int left=0;
            int right=ch.length-1;
            while(left<right){
                char temp = ch[left];
                ch[left]=ch[right];
                ch[right]=temp;
                left++;
                right--;
            }
            sb.append(String.valueOf(ch)+" ");
        }
        return sb.toString().trim();        
    }
}