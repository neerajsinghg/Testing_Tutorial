package string_java;

//Question 13: Write a Java program to count the number of lines, words, and characters in a text file.

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class CountWordsInFile {
public static void main(String[] args) throws IOException 
{
int nl = 0, nw = 0, nc = 0;
String line;
FileReader fr = new FileReader("D:\\textfile.txt");
BufferedReader br = new BufferedReader(fr);
while((line = br.readLine()) != null)
{
nl++;
nc += line.length();
StringTokenizer st = new StringTokenizer(line);
nw += st.countTokens();
}
System.out.printf("Number of lines: \t %d", nl);
System.out.printf("\nNumber of words: \t %d", nw);
System.out.printf("\nNumber of characters: \t %d", nc);
}
}
//Output:
//Number of lines:	 2
//Number of words:	 9
//Number of characters: 37
