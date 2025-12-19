package src.smartpractice;
import java.util.HashSet;
class NonDuplicateValue{
    public static void main(String[] args){
        int [] no = {2,3,4,3,2};//4
        
        HashSet<Integer> hs = new HashSet<>();
        HashSet<Integer> hs1 = new HashSet<>();
        for(int num : no){
            if(!hs.add(num)){
                 hs1.add(num);
            }
            
        }System.out.println(hs);
        System.out.println(hs1);
        hs.removeAll(hs1);
       
        System.out.println(hs);
    }
}
