import time
from tkinter import *
from main import *
# imorts to display image as a label
from PIL import Image, ImageTk
# check time from this side too
from datetime import datetime as dt
import random  #coz random is fun
import threading

alphabet = ('q','w','e','r','t','y','u','i','o','p',
          'a','s','d','f','g','h','j','k','l',
          'z','x','c','v','b','n','m', ' ')
# timer = timer

window = Tk()
runs = 0
# wordlist = wordlist
window.title("Typing Speed")
window.geometry("800x600")
window.config(padx=10, pady=10, bg="black")

canvas = Canvas(width=780, height=580, bg="black")
canvas.pack()

# text area
entry = Text(window,
             width=82,
             height=12,
             bg="#1ce9f4",
             highlightthickness=2,
             font=("chalkboard", 16, "normal")
             )
entry.place(x=20, y=20)

# text and typing stats
timer_label = Label(text= "00:00",
                   font=("Digital dream narrow", 15, "normal"),
                   bg='black',
                   fg=random.choice(['white', 'red','green', 'yellow'])
                   )
timer_label.place(x=20, y=290)

word_label = Label(text='',
                   font=("Courier", 15, "normal"),
                   bg='black',
                   fg=random.choice(['white', 'red','green', 'yellow'])
                   )
word_label.place(x=150, y=290)

speed_label = Label(text="Typing Speed:",
                    font=("Courier", 15, "normal"),
                    bg="black",
                    fg="light green")
speed_label.place(x=400, y=290)


# Keyboard image
# image = PhotoImage(file="images/keyboard.gif") couldn't open "images/keyboard.gif": no such file or directory
img = Image.open("images/keyboard.gif")
img = img.resize((740,300))
image = ImageTk.PhotoImage(img)

canvas.create_image(390, 300, anchor='n', image=image)

# handle or capture keystrokes
def key_handler(event=None):

    global runs
    global wordlist
    # global timer
    # if timer > 9:
    #     timer = f"00:{timer}"
    # else:
    #     timer = f"0):0{timer}"
    # timer_label.config(text=timer)
    if runs != 2:
        if event:    #and event.keysym in alphabet:
            # 0 to start by loading word and timer
            # 1 to keep the session going
            # 2 to end the session

            if runs == 0:
                # entry.config(state=NORMAL)
                start_timer()
                wordlist = load_words()
                # countdown(window)
                # check_activity(entry)
                # thread = threading.Thread(target=check_activity, args=[entry])
                # thread.start()
                # print("from gui",len(wordlist))
            if event.char == ' ':
                print('space')
                get_text(entry=entry)
            # make random generations
            else:
                random_speed = random.randint(1, 1200)
                # if len(wordlist) != 0:
                random_word = random.choice(wordlist)
                word_label.config(text=random_word)
                speed_label.config(text=f"Typing Speed: {random_speed} Words per Minute")

            # print(event.keysym)
            runs = 1

        if dt.now() >= end_time:
            # place end of ame logic
            final_speed = measure_speed()
            entry.delete('1.0', END)
            entry.insert(END, "TEST COMPLETE!")
            entry.config(state=DISABLED)
            speed_label.config(text=final_speed)

            runs = 2
    else:
        time.sleep(10)
        runs = 0
        entry.config(state='normal')
        entry.insert(END, "")

#   bind the window function to be able to read the keys
window.bind('<Key>', key_handler)

window.mainloop()
