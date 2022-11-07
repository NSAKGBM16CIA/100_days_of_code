//import java.lang.Math;

import java.util.*;
import java.util.Collections;
import java.util.Scanner;

public class PasswordGenerator {
//    #Password Generator Project

    private static char[] letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    private static char numbers[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    private static char symbols[] = {'!', '#', '$', '%', '&', '(', ')', '*', '+'};
    private static ArrayList<String>  password = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to the PyPassword Generator!");
        System.out.println("How many letters would you like in your password?\n");
        int nr_letters = scanner.nextInt();
        System.out.println("How many symbols would you like?\n");
        int nr_symbols = scanner.nextInt();
        System.out.println("How many numbers would you like?\n");
        int nr_numbers = scanner.nextInt();

//            #Eazy Level - Order not randomised:
//            #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
//
//
//            #Hard Level - Order of characters randomised:
//            #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
//        check whats needed more letters or symbols using multiple ternary operator
//        int length = nr_letters > nr_symbols ? nr_letters : nr_symbols> nr_numbers ? nr_symbols: nr_numbers;

        for (int i = 0; i < nr_letters; i++) {
            int index = (int)(Math.random()*letters.length);
            password.add(""+letters[index]);
        }
//        System.out.println("Your letters are: "+ password);
        for (int i = 0; i < nr_symbols; i++) {
            password.add(""+symbols[(int)(Math.random()*symbols.length)]);
        }
//        System.out.println("Your symbols are: "+ password);
        for (int i = 0; i < nr_numbers; i++) {
            password.add(""+numbers[(int)(Math.random()*numbers.length)]);
        }
      System.out.println("Your original password: "+ password);

//        List<String> pass_list = Arrays.asList(password);
        Collections.shuffle(password);
        StringBuilder final_password = new StringBuilder();
        for (String c : password){
            final_password.append(c);
        }


        System.out.println("Your password is: "+ final_password.toString());
    }
}
