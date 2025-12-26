# **ROCK-PAPER-SCISSORS**

### 

### **Overview**

* ###### This is a simple Rock–Paper–Scissors game built using Python’s Tkinter library for the graphical user interface (GUI).
* ###### The user selects one of the three options — Rock, Paper, or Scissors — and the computer randomly picks its move. The game then displays the result of each round directly in the window.



### **Features**

* ###### Interactive and beginner-friendly GUI using Tkinter.
* ###### Randomized computer moves using Python’s random module.
* ###### Instant feedback after each round.
* ###### Lightweight and easy to run — no external dependencies.



### **Game Rules**

* ###### Rock smashes Scissors → Rock wins.
* ###### Scissors cut Paper → Scissors win.
* ###### Paper covers Rock → Paper wins.
* ###### If both the player and the computer choose the same option → The round is a tie.



### **How to Run**

1. ###### Make sure you have Python 3.6+ installed on your system.
2. ###### Save the provided Python script as rock\_paper\_scissors.py.
3. ###### Open a terminal or command prompt and navigate to the script’s directory.
4. Run the script using:
   -python rock\_paper\_scissors.py
   ---
5. ###### A Tkinter window will appear where you can click Rock, Paper, or Scissors to play.



### **Code Breakdown**

* ###### tkinter: Used for creating and displaying the window and buttons.
* ###### random: Generates the computer’s choice randomly from the available list.
* ###### play() function: Determines the winner based on user and computer moves, then displays the result on screen.
* ###### GUI components:

###### &nbsp; -Label: Displays instructions and results.

###### &nbsp; -Button: Lets the user choose between Rock, Paper, or Scissors.



### **Future Improvements**

* ###### Improving the stacking of results by clearing or updating the label instead of creating a new one each time.
* ###### Adding score tracking to make gameplay more engaging.
