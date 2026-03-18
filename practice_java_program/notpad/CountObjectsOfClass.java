public class CountObjectsOfClass{
	public static int count=0;
	CountObjectsOfClass(){
		count++;
	}
	public static void main(String[] args){
		CountObjectsOfClass oc1 = new CountObjectsOfClass();
		CountObjectsOfClass oc2 = new CountObjectsOfClass();
		CountObjectsOfClass oc3 = new CountObjectsOfClass();
		CountObjectsOfClass oc4 = new CountObjectsOfClass();
		
		System.out.println(count);
	}
}