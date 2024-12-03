#Rock paper scissors GUI
from tkinter import *
import random
import os

w = Tk()
w.title("Rock Paper Scissors")
bg_color = "#282828"
w.config(bg=bg_color)
w.resizable(width=False, height=False)

#Fonts
fonts = ("Cascadia Code", 24)
#Random
rps = ["Rock", "Paper", "Scissors"]
computer = random.choice(rps)


#Labels and headings
you = Label(w, text="You choose:", font=fonts, fg="white", bg=bg_color)
bot = Label(w, text="Computer chooses:", font=fonts, fg="white", bg=bg_color)
bot_choice = Label(w, text="{}".format(computer), fg="white", bg=bg_color, font=fonts)

win = Label(w, text="You win", fg="green", bg=bg_color, font=fonts)
lose = Label(w, text="You lose", fg="red", bg=bg_color, font=fonts)
draw = Label(w, text="Draw", fg="white", bg=bg_color, font=fonts)

result = Label(w, text="Result:", fg="white", bg=bg_color, font=fonts)

#Functions for winning and losing
def rock():
    bot_choice.grid(row=1, column=2, padx=10, pady=10)
    if computer == rps[0]:
        #print("Draw")
        draw.grid(row=1, column=1, padx=10, pady=10)

    elif computer == rps[1]:
        #print("Computer wins")
        lose.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[2]:
        #print("You win")
        win.grid(row=1, column=1, padx=10, pady=10)
    rock['state'] = 'disabled'
    paper['state'] = 'disabled'
    scissors['state'] = 'disabled'

def paper():
    bot_choice.grid(row=1, column=2, padx=10, pady=10)
    if computer == rps[0]:
        #print("You win")
        win.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[1]:
        #print("Draw")
        draw.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[2]:
        #print("Computer wins")
        lose.grid(row=1, column=1, padx=10, pady=10)
    rock['state'] = 'disabled'
    paper['state'] = 'disabled'
    scissors['state'] = 'disabled'

def scissors():
    bot_choice.grid(row=1, column=2, padx=10, pady=10)
    if computer == rps[0]:
        #print("Computer wins")
        lose.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[1]:
        #print("You win")
        win.grid(row=1, column=1, padx=10, pady=10)
    elif computer == rps[2]:
        #print("Draw")
        draw.grid(row=1, column=1, padx=10, pady=10)
    rock['state'] = 'disabled'
    scissors['state'] = 'disabled'
    paper['state'] = 'disabled'
    
def restart():
    w.destroy()
    os.system("python main.py")

#Three buttons for rock paper and scissors
rock = Button(w, text="Rock", font=fonts, command=rock)
paper = Button(w, text="Paper", font=fonts, command=paper)
scissors = Button(w, text="Scissors", font=fonts, command=scissors)

#Restart Button
restart = Button(w, text="Reset", font=fonts, command=restart)

#Positions
#Buttons
rock.grid(row=1, column=0, padx=10, pady=10)
paper.grid(row=2, column=0, padx=10, pady=10)
scissors.grid(row=3, column=0, padx=10, pady=10)
restart.grid(row=3, column=1, padx=10, pady=10)
#label
you.grid(row=0, column=0, padx=10, pady=10)
bot.grid(row=0, column=2, padx=10, pady=10)
result.grid(row=0, column=1, padx=10, pady=10)

w.mainloop()
