import java.util.Scanner;

public class Main {
    //setting a Class (static) char variable X that will be used to start the game. accessible by main method.
    static char turn = 'X';



    public static void main(String[] args) {
        //initializing an empty char array with empty string. This will be used to append user input "X" or "O"
        char[] pos = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};


        //have to make game continuous, so putting this into a while loop which will break later
        while  (true) {

            //created a new scanner object and initialized two instance variables
            Scanner scan = new Scanner(System.in);
            int input;
            int count = 1;

            //do-while ensure everything in do will execute at least once
            //after input was init'd, will pass integer user input next. program will crash if int isn't passed
            do {
                System.out.print("What is your position? Player - " + turn + ".");
                System.out.print("\nChoose 1-9: ");
                input = scan.nextInt();
                
            } while (pos[input -1] == 'X' || pos[input - 1] == 'O');

            //starts initial input as 'X' based on integer positions of 1-9
            //using pos[input - 1] bc we array starts at pos[0], but we are only giving them positions 1-9
            pos[input - 1] = turn;

            //creating a tic-tac-toe grid based on positions 0 - 9
            //positions will not be filled in the array until the user selects the integer associated with that position
            System.out.println(" " + pos[6] + " | " + pos[7] + " | " + pos[8] + " ");
            System.out.println("---+---+---");
            System.out.println(" " + pos[3] + " | " + pos[4] + " | " + pos[5] + " ");
            System.out.println("---+---+---");
            System.out.println(" " + pos[0] + " | " + pos[1] + " | " + pos[2] + " ");

            //listing out all the possible option to win tic-tac-toe based on our grid we created abouve
            if (pos[0] == turn && pos[1] == turn && pos[2] == turn
                || pos[3] == turn && pos[4] == turn && pos[5] == turn
                || pos[6] == turn && pos[7] == turn && pos[8] == turn
                || pos[0] == turn && pos[3] == turn && pos[6] == turn
                || pos[1] == turn && pos[4] == turn && pos[7] == turn
                || pos[2] == turn && pos[5] == turn && pos[8] == turn
                || pos[0] == turn && pos[4] == turn && pos[8] == turn
                || pos[6] == turn && pos[4] == turn && pos[2] == turn) {
                System.out.println(turn + " won the game!");
                break;
            }

            //this will change the turns from "X" to "O"
            if (turn == 'X') {
                turn = 'O';
            }
            else if (turn == 'O') {
                turn = 'X'; }
            count++;

            //this is used to kill the loop if all the positions have been filled
            if (count > 9) {
                System.out.print("It is a draw. Restart the game.");
                break;
            }
            }

        }


    }





