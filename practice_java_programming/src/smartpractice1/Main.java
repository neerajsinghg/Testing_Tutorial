package src.smartpractice1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		 //String[] str = {"1","10","2","5","a","z","c","f","h"};
	        
	     //  char[] str = {1, 10, 2, 5, 'a', 'z', 'c', 'f', 'h'};
	       List<Object> obj = Arrays.asList(1, 10, 2, 5, 'a', 'z', 'c', 'f', 'h');//sort this and pahle alphabet bad me integer aaya
	       List<Integer> l = new ArrayList<>();
	       List<Character> l1 = new ArrayList<>();
	       
	       for(Object obj1: obj) {
	    	   if(obj1 instanceof Integer) {
	    		 l.add((Integer)obj1) ; 
	    	   }
	    	   else {
	    		   l1.add((Character)obj1);
	    	   }
	       }
	       Collections.sort(l1);
	       Collections.sort(l);
	       List<Object> l2 = new ArrayList<>();
	       
	       l2.addAll(l1);
	       l2.addAll(l);
	       System.out.println(l2);
	       
	       
	}

}
