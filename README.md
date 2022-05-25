# Jumper
Starter template for the Jumper game
Update the readme with the rules for the game and the name of your team members.

# Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

Rules
Jumper is played according to the following rules.

The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over.

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 seeker 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- jumper              (source code for game)
  +-- game 
    +-- director          (specific classes) 
    +-- jumper         (specific classes)
    +-- parachute           (specific classes)
    +-- terminal_service         (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* Baron Tshibasu
* Moises Parra Lozano
* Siarhei Herman
* Michael Porter Oleson




**To Do**

  **Coding That Needs Done**

      In Director:

        In do_updates:
          add else function at the end of the if block
            This will add one to the parachute's counter
            That should tell the parachute class to remove a line from the drawing

        In do_outputs:

          Add everything!

          Print out the current state of the parachute

          If the parachute's counter is too high, is_playing = False and print the "You lost" message

          If the word is solved, is_playing = False, print the word and the "You won" message


      In Card: (Everything is done I think)


      In Parachute:

        Add everything!

        Attribute: Make a list that has each diagram of the parachute, one line per entry.
        
        Attribute: Make a counter that tracks how many times we've guessed wrong.

        Method: Print as many lines in the diagram as (length of diagram array - counter)


  **Fluff That Needs Done**

    Update Readme with rules and team contributors

    Update methods in Director with proper comments

    Update methods in Word with proper comments

    Update methods in Parachute with proper comments


