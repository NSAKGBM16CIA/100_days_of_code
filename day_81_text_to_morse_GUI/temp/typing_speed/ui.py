from tkinter import *
# imorts to display image as a label
from PIL import Image, ImageTk

window = Tk()
window.title("Typing Speed")
window.geometry("800x600")
window.config(padx=10, pady=10, bg="black")

# canvas = Canvas(width=480, height=380, bg="black")

# text area
entry = Text(window,
             width=70,
             height=10,
             bg="#1ce9f4",
             highlightthickness=0
             )
entry.grid(row=0, columnspan=35)

# black bar in between to create a bit of space
bar_image = Image.open("images/black_bar.png")
bg_img = bar_image.resize((780, 50))
bar_photo = ImageTk.PhotoImage(bg_img)
b_label = Label(window, image=bar_photo, borderwidth=0, highlightthickness=0)
b_label.image = bar_photo
b_label.grid(row=1)

# bg-image
image = Image.open("images/keyboard_bg.png")
img = image.resize((780,300))
bg_photo = ImageTk.PhotoImage(img)

# the image wont display unless placed in a package that supports images eg Label
label = Label(window, image=bg_photo, borderwidth=0, highlightthickness=0)
label.image = bg_photo
label.grid(row=2)

window.mainloop()