from tkinter import *
from tkinter import messagebox
import time 
import random
# import package to generate random words
from random_word import RandomWords

FONT = "Helvetica"
BG_COLOR = "#a2d0c1"

cpm = 0
missed = 0
counter = 60
rw = RandomWords()
words = rw.get_random_words(minLength = 3, maxLength = 7, limit = 200)
word = words[random.randint(0, 199)]


def generate_word():
    word = words[random.randint(0, 199)]
    word_label.config(text = word)
         
def start_timer():
    global counter, cpm
    timer_label.config(text = counter)
    if counter > 0:
        counter -= 1
        timer = window.after(1000, start_timer)
    else:
        timer_label.config(text = "00")
        game_over_label.config(text =
         f"Time's Up!\nYou typed {cpm} characters correct\nYour score is {cpm/5} WPM")
        retry = messagebox.askretrycancel("Time's Up!", "Do you want to retry?")
        if retry:
            cpm = 0
            missed = 0
            counter = 60
            timer_label.config(text = counter)
            game_over_label.config(text = "Start the timer and \nafter typing the word press Enter")
            generate_word()
            player_entry.delete(0, END)
        else:
            window.quit()

def game(event):
    global cpm, missed
    for ind, char in enumerate(word_label["text"]):
        try:
            if player_entry.get()[ind] == char:
                cpm += 1
            else:
                missed += 1
        # if entry word is shorter than word in word_label
        # the index error will be raised
        except IndexError:
            continue
    generate_word()
    player_entry.delete(0, END)

    
window = Tk()
window.title("Type Speed")
window.minsize(width = 600, height=500)
window.config(bg = BG_COLOR)
window.resizable(width = False, height = False)

timer_label = Label(text = counter, bg = BG_COLOR, font = (FONT, 40, "bold"))
timer_label.place(x = 280, y = 40)
game_over_label = Label(text = "Start the timer and \nafter typing the word press Enter", bg = BG_COLOR, font = (FONT, 18))
game_over_label.place(x = 140, y = 400)
word_label = Label(text = word, bg = BG_COLOR, font = (FONT, 18))
word_label.place(x = 310, y = 200, anchor="center")

start_button = Button(text = "Start Timer", command = start_timer)
start_button.place(x = 280, y = 310)

entry_text = StringVar() 
entry = entry_text.get()

player_entry = Entry()
player_entry.config(bg = '#eff7e1', width = 24, font = (FONT, 18), justify='center')
player_entry.place(x = 150, y = 250)
player_entry.focus_set()

window.bind('<Return>', game)


window.mainloop()