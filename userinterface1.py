#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:18:01 2018

@author: YIWEN, HUY, KRISTIE, QUAN
"""


from appJar import gui #imports the gui library from appJar

"""
This is the function that determines code executed when each button is pressed

QUIZ ITEM:  Each teammember should replace the Button name (e.g. Button 1) and 
text to be displayed using the print statement.  Note that the Button name should
match the Button names in the gui definition starting on line 37.

Add code for your functions after each print statement

"""
print("Yiwen, Quan, Kristie, Huy")


def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Dice Rolling Game":
        app.infoBox("b1","this is our first game, dice rolling")
       # this game will be created by Quan and Yiwen 
        
    elif btn == "Snake Game":
        app.infoBox("b1","this is our second game, Snake game")
       #this game will be created by Huy and Kristie 
        

        
     
    else:
        print('Pick a valid option')

"""
The code below defines the gui, adding buttons, labels, images, color, etc.

QUIZ ITEM: Make changes to the title (line 37), image (line 39), and button
names (lines 42-46)

"""

app=gui("Main Menu","900x500")

#Replace "Blank Team" with your team name in line 41

app.addLabel("title", "Welcome to Snake Team's Game Menu")
app.setLabelBg("title", "blue")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in line 47

app.addImage("decor","snake.gif")
app.setFont(16)

#change the names Button 1-5 with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Dice Rolling Game", press)
app.addButton("Snake Game", press)

app.addButton("Exit",press)
app.go() #displays the gui


