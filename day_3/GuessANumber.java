import java.util.Scanner;

public class GuessANumber {
    int number = 0;
    int easyLevel = 10;
    int hardLevel = 5;
    int chances = 0;

    void generateNum(){
        number = (int)(Math.random()*100);
    }

    int guessNum(){
        chances -= 1;
        System.out.println("Guess the number: \n");
        Scanner scanner = new Scanner(System.in);
        int guess = scanner.nextInt();
        return guess;
    }

    void checkGuess(int guess){
        if(guess == number){
            printResults("won");
        }
        else if(guess < number){
            printResults("low");
        }
        else if(guess > number){
            printResults("high");
        }
    }

    void printResults(String status){
        if(status.equals("won")){
            System.out.println("You got it!! The answer was " +number);
            replay();
            return;
        }
        else if(status.equals("low")){
            if(chances != 0)
            System.out.println("That's too low! Try again...");
        }
        else if(status.equals("high")){
            if(chances !=0 )
            System.out.println("That's too high! Try again...");
        }
        if(chances == 0){
            System.out.println("Game Over! You ran out of lives. The number was " + number);
            replay();
            return;
        }
        System.out.println("You now have "+chances + " chances to get the number");
        checkGuess(guessNum());
    }

    private void replay() {
        System.out.println("Do you want to go again? y/n");
        String playAgain = new Scanner(System.in).nextLine().toLowerCase();

        if(playAgain.equals("y")){
            System.out.println("I am thinking of a number between 1 and 100");
            System.out.println("Pick a Level: Type 1 for 'Easy' or 2 for 'Hard':\n");
            new GuessANumber().start();
        }
        else {
            System.out.println("Loser!");
        }
    }

    void start(){
        int level = new Scanner(System.in).nextInt();
        if(level == 1){
            chances = 10;
            System.out.println("Good Choice! You have "+chances + " chances to get the number");
        }
        else {
            chances = 5;
            System.out.println("Good Choice! You have "+chances + " chances to get the number");
        }
        generateNum();
        checkGuess(guessNum());
    }

    public static void main(String[] args) {
        GuessANumber gan = new GuessANumber();
        System.out.println("I am thinking of a number between 1 and 100");
        System.out.println("Pick a Level: Type 1 for 'Easy' or 2 for 'Hard':\n");
        gan.start();

    }
}
