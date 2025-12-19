package src.smartpractice;
import java.io.*;
public class InputStream1 {

	public static void main(String[] args) {
		try {
		FileInputStream fis = new FileInputStream("D:\\eclipse\\java_question1\\src\\smartpractice\\java.txt");
		int i;
		while( (i= fis.read()) !=-1) {
			System.out.print((char)i);
		}
		fis.close();
		}
		catch(IOException e){
			e.printStackTrace();
		}

	}

}
