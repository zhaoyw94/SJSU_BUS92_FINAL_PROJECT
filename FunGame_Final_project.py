# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:40:22 2018

@author: zhaoy
"""

# -*- coding: utf-8 -*-

"""
Created on Fri Nov  14 17:30:34 2018

@author: Yiwen, Quan, Kristie, Huy
"""

"""
TEAM MEMBER: YIWEN ZHAO
             KRISTIE NGUYEN
             QUAN GAN
             HUY PHAM


"""

import tkinter
from time import sleep
from appJar import gui #imports the gui library from appJar
import time
import csv
import pandas
import turtle
import random
from random import randint



def get(lob):            
    lob = app.getOptionBox("Player Current Score for Games")
    lob == 0 
    if lob == "TurtleGame":           
        #app.infoBox("Result","Please type user's username")
        findname = app.stringBox("Find player score","Enter Your Username")
    #reads the csv file and assigns it to the dataframe named namesfr    
        namesfr = pandas.read_csv("Leaderboard222.csv")
    #finds the username based on the user entered first name
        answers = namesfr[namesfr.Username==findname].Tscore
    #conversion of the search result to a list
        answers1 = answers.tolist()
    #displays to search result in a popup
        app.infoBox("Your DateEnter is",answers1)
    elif lob == "ColorGame":
        #app.infoBox("b1","Please type user's username")
        findname = app.stringBox("Find player  score","Enter Your Username")
    #reads the csv file and assigns it to the dataframe named namesfr    
        namesfr = pandas.read_csv("Leaderboard222.csv")
    #finds the username based on the user entered first name
        answers = namesfr[namesfr.Username==findname].Cscore
    #conversion of the search result to a list
        answers1 = answers.tolist()
    #displays to search result in a popup
        app.infoBox("Player score is",answers1)  

def press(btn):
    
    if btn == "Exit":
        app.stop()
        
    elif btn == "Create Your ID To Play Games":
        
        fullname = app.stringBox("UserName","Enter Your Full Name \(Ex: Huy Pham)")
        username = app.stringBox("UserID","Creat Your Own Username \(huyffam11)")
        gender = app.stringBox("Gender","Enter Your Gender")
        date = app.stringBox("Date","Enter the date")
        with open('Leaderboard222.csv', 'a', newline='') as testfile:
             writer = csv.writer(testfile)
             writer.writerow([fullname,username,gender,date])    
             
        
    elif btn == "Color Game":
        app.infoBox("Color Game","Please input your Username before you play, so the game can record your score !")
        uname1 = app.stringBox("Please enter your Username","Enter the Username")
        def addname(uname1):
            csv.writer(open("Leaderboard222.csv", mode = 'a', newline = '')).writerow(uname1)
        #the list of possible colour.
        colours =     ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
        #the player's score, initially 0.
        score=0
        #the game time left, initially 30 seconds.
        timeleft=30
        
        #a function that will start the game.
        def start_Game(event):
        
            #if there's still time left...
            if timeleft == 30:
                #start the countdown timer.
                count_down()
        
            #run the function to choose the next colour.
            next_Colour()
        
        #function to choose and display the next colour.
        def next_Colour():
        
            #use the globally declared 'score' and 'play' variables above.
            nonlocal score
            nonlocal timeleft
        
            #if a game is currently in play...
            if timeleft > 0:
        
                #...make the text entry box active.
                e.focus_set()
        
                #if the colour typed is equal to the colour of the text...
                if e.get().lower() == colours[1].lower():
                    #...add one to the score.
                    score += 1
        
                #clear the text entry box.
                e.delete(0, tkinter.END)
                #shuffle the list of colours.
                random.shuffle(colours)
                #change the colour to type, by changing the text _and_ the colour to     a random colour value
                label.config(fg=str(colours[1]), text=str(colours[0]))
                #update the score.
                scoreLabel.config(text="Score: " + str(score))
                namesdf = pandas.read_csv("Leaderboard222.csv")
                namesdf.loc[namesdf["Username"]==uname1, "Cscore"] = score
                namesdf.to_csv("Leaderboard222.csv", index=False) 
        
        #a countdown timer function. 
        def count_down():
        
            #use the globally declared 'play' variable above.
            nonlocal timeleft
        
            #if a game is in play...
            if timeleft > 0:
        
                #decrement the timer.
                timeleft -= 1
                #update the time left label.
                timeLabel.config(text="Time left: " + str(timeleft))
                #run the function again after 1 second.
            timeLabel.after(1000, count_down)
        
        #create a GUI window.
        root = tkinter.Tk()
        #set the title.
        root.title("Color Game!")
        #set the size.
        root.geometry("")
        
        #add an instructions label.
        instructions = tkinter.Label(root, text="Type in the colour of the words", font=('Times', 14))
        instructions.pack()
        
        #add a score label.
        scoreLabel = tkinter.Label(root, text="Press enter to start", font=    ('Times', 14))
        scoreLabel.pack()
        
        #add a time left label.
        timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=    ('Times', 14))
        timeLabel.pack()
        
        #add a label for displaying the colours.
        label = tkinter.Label(root, font=('Times', 60))
        label.pack()
        
        #add a text entry box for typing in colours.
        e = tkinter.Entry(root)
        #run the 'startGame' function when the enter key is pressed.
        root.bind('<Return>', start_Game)
        e.pack()
        #set focus on the entry box.
        e.focus_set()
        
        #start the GUI
        root.mainloop()
                
                
                
    elif btn == "Snake game leader board":
        
        fullname = app.stringBox("Name","Enter Your Full Name")
        username = app.stringBox("UserName","Enter Your Username")
        gender = app.stringBox("Gender","Enter Your Gender")
        date = app.stringBox("Date","Enter the date")
        with open('Leaderboard222.csv', 'a', newline='') as testfile:
             writer = csv.writer(testfile)
             writer.writerow([fullname,username,gender,date])        
   
    elif btn == "Turtle Game":
        app.infoBox("Turtle Game","Please input your Username before you play, so the game can record your score !")
        uname1 = app.stringBox("Please enter your username","Enter the Username")
        def addname(uname1):
            csv.writer(open("Leaderboard222.csv", mode = 'a', newline = '')).writerow(uname1)          
    
        delay = 0.1
    
    # Score
        score = 0
        high_score = 0
    
    # Set up the screen
        window = turtle.Screen()
        window.title("Collecting Wild Turtle")
        window.bgcolor("royal blue")
        window.setup(width=600, height=600)
        window.tracer(0) # Turns off the screen updates
    
    # Snake head
        snakehead = turtle.Turtle()
        snakehead.speed(5)
        snakehead.shape("circle")
        snakehead.color("black")
        snakehead.penup()
        snakehead.goto(0,0)
        snakehead.direction = "stop"
    
    # Snake food
        food = turtle.Turtle()
        food.speed(0)
        food.shape("turtle")
        food.color("green")
        food.penup()
        food.goto(0,100)
      
        segments = []
    
    # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Turtle: 0  Highest Turtle Score: 0", align="center", font=("Courier", 20, "normal"))
    
    # Functions
        def go_up():
            if snakehead.direction != "down":
                snakehead.direction = "up"
    
        def go_down():
            if snakehead.direction != "up":
                snakehead.direction = "down"
    
        def go_left():
            if snakehead.direction != "right":
                snakehead.direction = "left"
    
        def go_right():
            if snakehead.direction != "left":
                snakehead.direction = "right"
    
        def move():
            if snakehead.direction == "up":
                y = snakehead.ycor()
                snakehead.sety(y + 20)
    
            if snakehead.direction == "down":
                y = snakehead.ycor()
                snakehead.sety(y - 20)
    
            if snakehead.direction == "left":
                x = snakehead.xcor()
                snakehead.setx(x - 20)
    
            if snakehead.direction == "right":
                x = snakehead.xcor()
                snakehead.setx(x + 20)
    
    # Keyboard bindings
        window.listen()
        window.onkeypress(go_up, "Up")
        window.onkeypress(go_down, "Down")
        window.onkeypress(go_left, "Left")
        window.onkeypress(go_right, "Right")
    
    # Main game loop
        while True:
            window.update()
    
        # Check for a collision with the border
            if snakehead.xcor()>290 or snakehead.xcor()<-290 or snakehead.ycor()>290 or snakehead.ycor()<-290:
                time.sleep(1)
                snakehead.goto(0,0)
                snakehead.direction = "stop"
    
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
            # Clear the segments list
                segments.clear()
    
            # Reset the score
                score = 0
    
            # Reset the delay
                delay = 0.1
    
                pen.clear()
                pen.write("Turtle: {}  High Turtle Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal")) 
    
    
        # Check for a collision with the food
            if snakehead.distance(food) < 20:
            # Move the food to a random spot
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                food.goto(x,y)
    
            # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("turtle")
                new_segment.color("gold")
                new_segment.penup()
                segments.append(new_segment)
    
            # Shorten the delay
                delay -= 0.0000001
    
            # Increase the score
                score += 1
    
                if score > high_score:
                    high_score = score
            
                pen.clear()
                pen.write("Turtle: {}  Highest Turtle Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal")) 
                namesdf = pandas.read_csv("Leaderboard222.csv")
                namesdf.loc[namesdf["Username"]==uname1, "Tscore"] = score
                namesdf.to_csv("Leaderboard222.csv", index=False) 
        # Move the end segments first in reverse order
            for index in range(len(segments)-1, 0, -1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)
    
        # Move segment 0 to where the head is
            if len(segments) > 0:
                x = snakehead.xcor()
                y = snakehead.ycor()
                segments[0].goto(x,y)
    
            move()    
    
        # Check for head collision with the body segments
            for segment in segments:
                if segment.distance(snakehead) < 20:
                    time.sleep(1)
                    snakehead.goto(0,0)
                    snakehead.direction = "stop"
            
                # Hide the segments
                    for segment in segments:
                        segment.goto(1000, 1000)
            
                # Clear the segments list
                    segments.clear()
                    
                # Reset the score
                    score = 0
                    
                # Reset the delay
                    delay = 0.1
            
                # Update the score display
                    pen.clear()
                    pen.write("Turtle: {}  Highest Turtle Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
            time.sleep(delay)
    
        window.mainloop()
         

    
    elif btn == "Find Players Username":
        app.infoBox("b1","Please type user's name")       
        findname = app.stringBox("Find player's username","Enter Your Name")
#reads the csv file and assigns it to the dataframe named namesfr    
        namesfr = pandas.read_csv("Leaderboard222.csv")
#finds the username based on the user entered first name
        answername = namesfr[namesfr.Name==findname].Username
#conversion of the search result to a list
        answernamel = answername.tolist()
#displays to search result in a popup
        app.infoBox("Your Username is",answernamel)
#the following code mimics the one in the previous elif to    
   
    
    
    elif btn == "Display Usernames":
#reads the csv file and assigns it to the namesfr dataframe
        namesfr = pandas.read_csv("Leaderboard222.csv")
#assigns data from the first column to the firstnames object
        unames = namesfr.Username
#converts firstnames to a list
        unamesl = unames.tolist()
#establishes a subwindow called "one"
        app.startSubWindow("one")
        app.showSubWindow("one")    
        app.setSize(400,400)
        app.setLocation("CENTER")
#adds a Close button to the subwindow which calls the close() function
#when pressed
        app.addButton("Close",close)
#the following code adds a label to the subwindow for each
#item in the first column of the dataframe as assigned to
#firstnamesl
        count=1
        for first in unamesl:
            app.addLabel("label"+str(count),first)
            
            count = count+1
            
    else:
            print('Pick a valid option')
            
            
def close():
#stops and destroys to window so that you can re-create
#it from scratch with new data as needed
    app.stopSubWindow()
    app.destroySubWindow("one")  
       
            
    





"""
This section creates the Main Window, starting with a
Splash Screen then displaying the main window with
a graphic and buttons for each action.  When a button
is pressed, the press function (above) is called
""" 
app = gui("Grid Demo","500x800")
#shows a splashpage for a few seconds
app.setSticky("news")
app.setExpand("both")
app.showSplash("Welcome!!!", fill='green', stripe='black', fg='white', font=44)
app.addLabel("title", "Welcome to the Game Center")
app.setLabelBg("title", "black")
app.setLabelFg("title", "white")
#app.setBg("black")
app.addImage("decor","arcade.gif")
app.setImageSize("decor",800,500)




app.setFont(16)
#these are the buttons that call the press function
#note how the button names match each elif statement above
app.addButton("Create Your ID To Play Games", press)
app.setButtonBg("Create Your ID To Play Games", "black")
app.setButtonFg("Create Your ID To Play Games", "white")



app.addButton("Color Game", press)
app.setButtonBg("Color Game", "black")
app.setButtonFg("Color Game", "white")

app.addButton("Turtle Game", press)
app.setButtonBg("Turtle Game", "black")
app.setButtonFg("Turtle Game", "white")

app.addLabelOptionBox("Player Current Score for Games",["ColorGame","TurtleGame"],callFunction=True)
app.setLabelBg("Player Current Score for Games","black")
app.setLabelFg("Player Current Score for Games","white")
app.setOptionBoxBg("Player Current Score for Games","black")
app.setOptionBoxFg("Player Current Score for Games","white")


app.addButton("Submit", get)
app.setButtonBg("Submit", "black")
app.setButtonFg("Submit", "white")

app.addButton("Find Players Username", press)
app.setButtonBg("Find Players Username", "black")
app.setButtonFg("Find Players Username", "white")

app.addButton("Exit", press)
app.setButtonBg("Exit", "black")
app.setButtonFg("Exit", "white")
app.go()

