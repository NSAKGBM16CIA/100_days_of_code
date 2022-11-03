import java.util.Scanner;
import java.util.Arrays;

import static java.lang.Integer.parseInt;

public class TipCalculator {
//day two of 100 days of code I am working on this in java and python

        public static void main(String[]args){
            Scanner sc = new Scanner(System.in);
            System.out.println("Welcome to the Tip Calculator");
//        #Each person should pay (150.00 / 5) * 1.12 = 33.6
            System.out.println("What was the total bill?");
            String amt = sc.nextLine();
            int total = 0;
//                    parse string []$4.89 ['$','4','8','9']
            char[] amtChar = amt.toCharArray();
//40 [$'4'0']
            if (amt.charAt(0) == '$'){
                String s = "";
                char [] arr =  Arrays.copyOfRange(amtChar, 1, amtChar.length);
                StringBuilder sb = new StringBuilder();
                for (int c = 0 ; c < arr.length; c++){
                    sb.append(arr[c]);
                }
                s = sb.toString();
                total = Integer.valueOf(s);
//                System.out.println(s);
//                System.out.println(Integer.valueOf(s));
//                System.out.println(parseInt(s));
//                 total = Double.parseDouble(s); total will also have to n=be initialised as a double
            }
            else {
                total = Integer.valueOf(amt);
            }

        // #If the bill was $150.00, split between 5 people, with 12% tip.
            Scanner scanner = new Scanner(System.in);
            System.out.println("How many people are splitting the bill?");
            int numOfPeople = scanner.nextInt();

            System.out.println("How much percentage tip do you want to pay? \n 10%, 12% or 15%. \n Enter number without % sign");
            int tip = sc.nextInt();


//        #Format the result to 2 decimal places = 33.60
            double bill = total + (double)tip/100*total;  //4 4.0
            System.out.println("Bill :"+total); //f"{}"
            System.out.println("Bill + Tip: "+bill);
            String indiv_bill = String.format("%2.02f", bill/numOfPeople); //String.foramt("2..02f",varnaame)
            System.out.print("Each Person Pays: $"+indiv_bill);

//
//        #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.？
//
//        #Write your code below this line ？
        }
    }
