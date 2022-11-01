import java.util.Scanner;

public class BandNameGenerator {
    public static void main(String[]args){
//         the idea of the code is to get input concatnate and comment
//# I'm coding these projects as part of a 100-day challenge and I will code them both in python and Java


//#1. Create a greeting for your program.
        System.out.println("So you are starting a band? Let us get you a name for it!\n");
//#2. Ask the user for the city that they grew up in.
        Scanner sc = new Scanner(System.in);
        System.out.println("Which city did you grow up in?\n");
        String city = sc.nextLine();

//#3. Ask the user for the name of a pet.
        System.out.println("And, what is your pet\'s name?\n'");
        String pet = sc.nextLine();

//#4. Combine the name of their city and pet and show them their band name.
        System.out.println("Cool, You band name is: "+city +" "+ pet);

//#5. Make sure the input cursor shows on a new line, see the example at:
//#   https://replit.com/@appbrewery/band-name-generator-end
    }
}
/**
    Failed to create GitHub Repository
        422 Unprocessable Entity - Repository creation failed.
        [Repository; description]custom: description control characters are not allowed
 **/
