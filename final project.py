#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# add the appJar folder to your PATH
import sys
import random
sys.path.append("E:\PYLIB")

# main.py
from appJar import gui

# handle button events
def press(button):
    if button == "Leave":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if usr == 'abc' and pwd =='abc':
            print("Welcome to our games!")
            
            
            def main():
                game_start = input("Would you like to roll the dice?")
                if game_start == 'yes':
                    dice_roll()
                else:
                    print('how about try our snake game?')
                    
                    # put snake game codes here
                    
                    
                    
                    
                    
                    
            def dice_roll():
                while True:
                    
                    play_again = input("Would you like to play again? ")
                    if play_again == 'yes':
                        print("Your number is: " + str(random.randint(1,6)))
                    else:
                        print("Input not recognized")
                        app.stop()

            

            if __name__ == '__main__':
                main()
    
        else:
            print("Incorrect! Bye-Bye~~~~~~")
     
      

# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Wanna play small fun game?")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

# link the buttons to the function called press
app.addButtons(["Go", "Leave"], press)

app.setFocus("Username")

# start the GUI

app.go()  




 