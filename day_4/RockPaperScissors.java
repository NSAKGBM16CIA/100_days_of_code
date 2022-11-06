import java.util.Scanner;
import java.lang.Math;

public class RockPaperScissors {
     Scanner sc = new Scanner(System.in);
    private static int human_choice;
    private static int computer_choice;

    static String [] choice_names = {"rock", "paper", "scissors"};

    static  String [] choices_array = {
//            rock

            "_______\n"+
                    "   ---'   ____)\n"+
                    "        (_____)\n"+
                    "        (_____)\n"+
                    "        (____)\n"+
                    "  ---.__(___)\n"
            ,
//          # paper
            "               _______\n"+
                    "---'   ____)____\n"+
                    "         ______)\n"+
                    "        _______)\n"+
                    "        _______)\n"+
                    "       ---.__________)\n"
            ,

//            # scissors

            "_______\n"+
                    "---'   ____)____\n"+
                    "______)\n"+
                    "__________)\n"+
                    "(____)\n"+
                    "---.__(___)\n"
    };


     static void print_choices(){
        System.out.println("human choice " + choice_names[human_choice]+ " \n"+ choices_array[human_choice]);
        System.out.println("computer choice " + choice_names[computer_choice] + "\n" + choices_array[computer_choice]);

    }


    public static void main (String[]args){

//          # Write your code below this line ？
        System.out.println("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." );

        human_choice = new RockPaperScissors().sc.nextInt();

        int [] choices = {0, 1, 2};

        computer_choice = (int) (Math.random() * choices.length);


        if (human_choice == computer_choice){
            System.out.println("Draw");
            print_choices();
        }
        else if(human_choice == 0 & computer_choice == 1 || human_choice == 1 & computer_choice == 2 || human_choice == 2 & computer_choice == 0){
            System.out.println("You Lost");
            print_choices();
         }
        // else if (human_choice == 0 & computer_choice == 2 || human_choice == 2 & computer_choice == 1 || human_choice == 1 & computer_choice == 0){
        //     System.out.println("You won!");
        //  print_choices();
        // }
        else{
                System.out.println("You won!");
                print_choices();
            }


    }


}
