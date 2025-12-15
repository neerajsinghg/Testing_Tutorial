package java_question;

import java.util.Stack;

public class Stack1 {

	public static void main(String[] args) {
		
		Stack<String> stack = new Stack<>();
		stack.push("java");
		stack.push("coffee");
		stack.push("Book");
		System.out.println(stack.peek());
		System.out.println(stack);
		System.out.println(stack.search("java"));//top se kitna door hai

	}

}
