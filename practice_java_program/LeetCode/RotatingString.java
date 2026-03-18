//796. Rotate String
//Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
//A shift on s consists of moving the leftmost character of s to the rightmost position.
//For example, if s = "abcde", then it will be "bcdea" after one shift.
//Example 1:
//Input: s = "abcde", goal = "cdeab"
//Output: true
//Example 2:
//Input: s = "abcde", goal = "abced"
//Output: false

//Key Observation (Important Trick)
//If we concatenate s with itself:
//s = "abcde"
//s + s = "abcdeabcde"
//All possible rotations of s will appear inside this string.

class RotatingString{
    public static void main(String[] args){
	String s="abcde", goal="cdeab";
	System.out.println(rotateString(s,goal));
    }
    public static boolean rotateString(String s, String goal) {
        if(s.length() != goal.length()){
            return false;
        }
        String combined=s+s;
        return combined.contains(goal);
        
    }
}