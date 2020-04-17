import java.util.*;
public class c {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();

        StringBuilder reversedWordTmp = new StringBuilder(word);
        String reversedWord = reversedWordTmp.reverse().toString();

        printAllOddSubstrings(reversedWord);
    }

    public static void printAllOddSubstrings(String word) {
        String newWord = "";
        for (int i = 1; i < word.length(); i += 2) {
            newWord = newWord + word.charAt(i);
        }
        printAllSubstrings(newWord);
    }

    public static void printAllSubstrings(String word) {
        for (int i = 0; i < word.length(); i++) {
            System.out.println(word.substring(i));
        }
    }
}
