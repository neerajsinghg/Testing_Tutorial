package smartpractice1;

public class StaticVar {

	String name;// Instance Variables
	String address;
	static String city;//class variables
	 static int i;
	 static {
		 city="Bangalore";
		 i =0;
		 
	 }
	
	StaticVar(String name, String address)
	{
		this.name= name;
		this.address =address;
		i++;
		System.out.println(i);
		
		
		
	}
	public void getAddress()  //Instance methods
	{
		System.out.println(address+" "+city);
		
	}
	
	public static void getCity() //CLass methods
	{
		System.out.println(city);
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StaticVar obj =new StaticVar("Bob","Marthalli");
		StaticVar obj1 =new StaticVar("Ram","Jayangar");
		//StaticVar obj2 =new StaticVar("Ram","Jayangar");
		obj.getAddress();
		obj1.getAddress();
		StaticVar.getCity();
		StaticVar.i=4;
		obj.address="XYZ";
		
		
		
		
		
		
	}

}

