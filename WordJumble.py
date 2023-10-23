from tkinter import *
from random import *


root = Tk()
root.title("WORD JUMBLE")
root.geometry("600x400")


def shuffling():

    e.delete(0,END)
    answer_lbl.config(text="")
    
    hint_lbl.config(text='')

    global ctr
    ctr = 0

    fruits = [
            'APPLE',
            'BANANA',
            'GRAPES',
            'PINEAPPLE',
            'PAPYA',
            'ORANGE',
            'STRAWBERRIES',
            'WATERMELON',
            'PEACH',
            'MANGO',
            'LEMON',
            'TANGERINE'
        ]
    global word
    word = choice(fruits)
    #lbl.config(text=word)

    unjumble = list(word) #BREAKS THE LETTER AND SHOWS THEM IN A LIST
    shuffle(unjumble)

    global shuffled_word
    shuffled_word = ''
    for letter in unjumble:
        shuffled_word = shuffled_word + letter

    lbl.config(text=shuffled_word)


def answered():
    #if word == toUpper(e.get()):
    if word == e.get().upper():
        answer_lbl.config(text="HURRAY!! YOU ARE CORRECT")
    else:
        answer_lbl.config(text="NAH, YOU ARE WRONG.\nCORRECT WORD IS:"+word)



def hinted(count):
    global ctr
    ctr = count

    word_len = len(word)
    if ctr < word_len:
        hint_lbl.config(text=f'{hint_lbl["text"]} {word[ctr]}')
        ctr+=1

lbl = Label(root,text="",font=32)
lbl.pack(pady=20)

e = Entry(root,font=(20))
e.pack(pady=20)

btn_frame = Frame(root)
btn_frame.pack(pady=20)

btn = Button(btn_frame,text="PICK A WORD",command=shuffling)
btn.grid(row=2,column=1,padx=20)


answer = Button(btn_frame,text="ANSWER",command=answered)
answer.grid(row=2,column=2,padx=20)

answer_lbl = Label(root,text="",font=32)
answer_lbl.pack(pady=20)

hint = Button(btn_frame,text='HINT',command=lambda:hinted(ctr))
hint.grid(row=2,column=3,padx=20)

hint_lbl = Label(root,text='',font=20)
hint_lbl.pack()

mainloop()