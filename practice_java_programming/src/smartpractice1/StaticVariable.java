package src.smartpractice1;

public class StaticVariable {
	   static int a = 20;
	   static {
	        a++;
	   }
	   {
	     a++;
	     System.out.println(a);
	   }
	public static void main(String[] args) 
	{
	   StaticVariable obj = new StaticVariable();
	   StaticVariable obj2 = new StaticVariable();
	   StaticVariable obj3 = new StaticVariable();
	  }
	}


