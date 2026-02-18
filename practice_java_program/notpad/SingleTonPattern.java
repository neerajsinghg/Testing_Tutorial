public class SingleTonPattern{
    public static void main(String[] args) {

	SingleTon obj1 = SingleTon.getInstance();
	SingleTon obj2 = SingleTon.getInstance();

	System.out.println(obj1 == obj2);

	SingletonExample obj3 = SingletonExample.getInstance ();
	SingletonExample obj4 = SingletonExample.getInstance();

	System.out.println(obj3 == obj4);
        
    }
}
class SingleTon{
	private static SingleTon instance = new SingleTon();

	private SingleTon(){
		System.out.println("Singleton constructer called");
	}

	public static SingleTon getInstance(){
		return instance;
	}
}
//thread safe with synchronized singleton mathod
class SingletonExample {

    private static SingletonExample instance;

    private SingletonExample() {}

    public static synchronized SingletonExample getInstance() {
        if (instance == null) {
            instance = new SingletonExample();
        }
        return instance;
    }
}