package java_question1;

public class CountNoOfObjects {
	static int count=0;
	public CountNoOfObjects(){
		count +=1;
		//System.out.println(count);
	}
	public void display() {
		System.out.println(count);
	}

	public static void main(String[] args) {
		
		CountNoOfObjects c = new CountNoOfObjects();
		CountNoOfObjects cc = new CountNoOfObjects();
		CountNoOfObjects ccc= new CountNoOfObjects();
	
	cc.display();
	}

}
