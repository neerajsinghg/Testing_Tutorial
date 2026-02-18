import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadCSV{
    public static void main(String[] args) {
        String filePath = "F:\\Testing_Tutorial\\practice_java_program\\notpad\\Book1csv.csv";
        
        try{
		BufferedReader br = new BufferedReader(new FileReader(filePath));
		String line;

		while ((line=br.readLine())!=null){
			System.out.println(line); //print entire row
		}
		br.close();
	}
	catch (IOException e){
		e.printStackTrace();
	}
    }
}