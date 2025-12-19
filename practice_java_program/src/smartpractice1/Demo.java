package smartpractice1;

 abstract class Animal1{
	
	abstract void dog();
	void cat() {
		System.out.println("this is cat ");
	}
	void monkey() {
		System.out.println("this is monkey ");
	}}
	
	class Wild extends Animal1{
		
		void dog() {
			System.out.println("this is dog");
		}
		//Animal a = new Wild();
		
		
	}

public class Demo {
	public static void main(String[] args) {
		Wild a = new Wild();
		a.cat();
		a.dog();
		a.monkey();
	}
}
	


