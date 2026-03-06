import java.util.*;
public class AleternetNumberReverse{
    public static void main(String[] args){
        int[] number = {1,2,3,4,5,6,7,8,9};
        ArrayList<Integer> al1 = new ArrayList<>();
        ArrayList<Integer> al2 = new ArrayList<>();
        for(int i=0; i<number.length; i++){
            if(i%2==0){
                al1.add(number[i]);
            }
            else{
                al2.add(number[i]);
            }
        }
        System.out.print(al1+" "+al2);
        
        Collections.reverse(al1);
        Collections.reverse(al2);
        System.out.println();
        System.out.print(al1+" "+al2);
        
        ArrayList<Integer> al = new ArrayList<>();
        int eindex=0;
        int oindex=0;
        for(int i=0; i<number.length; i++){
            if(i%2==0){
                al.add(al1.get(eindex));
                eindex++;
            }
            else{
                al.add(al2.get(oindex));
                oindex++;
            }
        }
        System.out.println();
        System.out.println(al);
    }
}

//[1, 3, 5, 7, 9] [2, 4, 6, 8]
//[9, 7, 5, 3, 1] [8, 6, 4, 2]
//[9, 8, 7, 6, 5, 4, 3, 2, 1]