

let chances = 0;
var number = 0;
var easy_level = 10;
var hard_level = 5;



function generate_num(){
    number = Math.floor(Math.random()*101);
}

function guess_num(){
    chances -= 1;
    guess = parseInt(prompt("Guess the number{ \n"));
    return guess;
}

function check_guess(guess){
    if (guess == number){
        print_results("won");
        }
    else if (guess < number){
        print_results("low");
        }
    else if (guess > number){
        print_results("high");
        }
      }


function print_results(status){
    if (status == "won"){
        console.log("You got it!! The answer was "+number);
        replay();
        return;
      }
    else if (status == "low"){
        if (chances != 0){
            console.log("That's too low! Try again...");
          }
        }
    else if (status == "high") {
        if (chances != 0){
            console.log("That's too high! Try again...");
          }
        if (chances == 0){
        console.log("Game Over! You ran out of lives. The number was "+number);
        replay();
        return;
      }
    }
  }
    // console.log("Good Choice! You have "+chances+ "chances to get the number");
    // check_guess(guess_num());


function replay(){
    play_again = prompt("Do you want to go again? y/n");
    if (play_again == "y"){
        start();
      }
    else{
        console.log("Loser!");

      }
    }


function start(){
    console.log("I am thinking of a number between 1 and 100");
    level = parseInt(prompt("Pick a Level Type 1 for 'Easy' or 2 for 'Hard'\n"));

    if (level == 1){
        chances = 10;
        console.log("Good Choice! You have "+chances+ " chances to get the number");
      }
    else{
        chances = 5;
        console.log("Good Choice! You have "+chances +"chances to get the number");
    generate_num();
    check_guess(guess_num());
  }
}

start();
