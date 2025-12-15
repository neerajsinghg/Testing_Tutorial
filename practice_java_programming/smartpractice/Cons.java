package smartpractice;

public class Cons {
	int a;
	int b;
	Cons(){
		System.out.println("this is default constructor");
	}
	Cons(int a, int b){
		this.a=a;
		this.b=b;
		int c=a+b;
		System.out.println(c);
	}
	Cons(int a){
		System.out.println(a);
	}

	public static void main(String[] args) {
		
		Cons d = new Cons(10);
		System.out.println(d);
	}

}
