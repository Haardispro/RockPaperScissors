#Rock paper scissors GUI
from tkinter import *
import random
import os
import time

w = Tk()
w.title("Rock Paper Scissors")
#w.geometry("800x600")
w.config(bg="#282828")

#Fonts
fonts = ("Cascadia Code", 24)
#Random
rps = ["Rock", "Paper", "Scissors"]
computer = random.choice(rps)
print(computer)

#Labels and headings
you = Label(w, text="You", font=fonts, fg="white", bg="#282828")
bot = Label(w, text="Computer", font=fonts, fg="white", bg="#282828")
bot_choice = Label(w, text="Computer chose {}".format(computer), fg="white", bg="#282828", font=fonts)

win = Label(w, text="You win", fg="green", bg="#282828", font=fonts)
lose = Label(w, text="You lose", fg="red", bg="#282828", font=fonts)
draw = Label(w, text="Draw", fg="white", bg="#282828", font=fonts)

#Functions for winning and losing
def rock():
    bot_choice.grid(row=1, column=2, padx=10, pady=10)
    if computer == rps[0]:
        print("Draw")
        draw.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[1]:
        print("Computer wins")
        lose.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[2]:
        print("You win")
        win.grid(row=1, column=1, padx=10, pady=10)
    #time.sleep(6)
    #w.destroy()
    #os.system("python another.py")
    #computer = random.choice(rps)

def paper():
    bot_choice.grid(row=1, column=2, padx=10, pady=10)
    if computer == rps[0]:
        print("You win")
        win.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[1]:
        print("Draw")
        draw.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[2]:
        print("Computer wins")
        lose.grid(row=1, column=1, padx=10, pady=10)
    #time.sleep(6)
    #w.destroy()
    #os.system("python another.py")

def scissors():
    bot_choice.grid(row=1, column=2, padx=10, pady=10)
    if computer == rps[0]:
        print("Computer wins")
        lose.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[1]:
        print("You win")
        win.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[2]:
        print("Draw")
        draw.grid(row=1, column=1, padx=10, pady=10)
    #time.sleep(6)
    #w.destroy()
    #os.system("python another.py")

#Three buttons for rock paper and scissors
rock = Button(w, text="Rock", font=fonts, command=rock)
paper = Button(w, text="Paper", font=fonts, command=paper)
scissors = Button(w, text="Scissors", font=fonts, command=scissors)

#Positions
#Buttons
rock.grid(row=1, column=0, padx=10, pady=10)
paper.grid(row=2, column=0, padx=10, pady=10)
scissors.grid(row=3, column=0, padx=10, pady=10)
#label
you.grid(row=0, column=0, padx=10, pady=10)
bot.grid(row=0, column=2, padx=10, pady=10)

w.mainloop()
