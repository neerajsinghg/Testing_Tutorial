package linkedlist;

import java.util.*;

public class LinkedList1 {

		    public static void main(String[] args) {
		   
		        List<String> list = new LinkedList<>();
		        list.add("John");               // index 0
		        list.add(1, "Herry");           // index 1
		        list.add(3, "Ivaan");           // ❗ ERROR here!
		        list.add("Deep");               // not reached if error occurs
		        System.out.println(list);

	}

}
