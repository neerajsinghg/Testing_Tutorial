//print array without null value
public class RemoveNullValue{
	public static void main(String[] args){
		Object[] array = {1,2,3,null,4,5,null,3};
		for(Object ar:array){
			if(ar==null){
				continue;
			}
			else{
				System.out.print(ar+" ");
			}
		}
	}
}