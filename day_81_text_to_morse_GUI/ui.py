import time
from tkinter import *
from tkinter import filedialog

from encoder import Encoder

encoder = Encoder()
window = Tk()
BG_COLOR1 = "#034285"
BG_COLOR2 = "#1f67b3"
window.title("Morse De-Encoder")
window.minsize(width=800, height=400)
window.resizable(width=False, height=False)
window.config(padx=0,pady=20, bg=BG_COLOR1)


# canvas layout
canvas = Canvas(window, width=800, height=380, highlightthickness=0, bg=BG_COLOR2)
canvas.pack()
# fill=BOTH, expand=True)

# logo image
logo_image = PhotoImage(file="images/logo.png")
canvas.create_image(400, 80, image=logo_image)

# buttons
text_entry = Entry(width=65)
text_entry.insert(END, "Type a phrase to translate instantly...")
text_entry.place(x=100, y=155)

clear_btn = Button(window,
                   text="Clear",
                   highlightthickness=2,
                   command=lambda: text_entry.delete(0, END)
                   )
clear_btn.place(x=705, y=158)

# pass text to convert
def pass_baton():
    text = text_entry.get().strip()
    if text != "":
        # print(f"text from entry {text}")
        text_entry.delete(0, END)
        # print(f"text from encoder {encoder.code(text)}")
        text_entry.insert(END, encoder.code(text))
        # update_label("Text Cleared!")


instant_img = PhotoImage(file="images/instant.png")
btn_img = instant_img.subsample(3, 3)
instant_btn = Button(window,
                     image=btn_img,
                     highlightthickness=1,
                     command=pass_baton)
instant_btn.place(x=250, y=200)

# uploading a file function
def upload_file():
    update_label("File Uploading...")
    file = filedialog.askopenfile()
    # print(file.name)
    if file != None:
        encoded = encoder.read_file(file.name)
        update_label("File Successfully Uploaded!")
        encoder.save_file(encoded)
    else:
        update_label("Error: Retry Uploading.")

# upload button
up_img = PhotoImage(file="images/upload.png")
upload_img = up_img.subsample(3, 3)
upload_btn = Button(image=upload_img, highlightthickness=1, command=upload_file)
upload_btn.place(x=250, y=250)

# decode file option
def decode_file():
    text = encoder.text
    update_label("Attempting Decoding...")
    time.sleep(3)
    if text != "":
        encoder.code(text)
        update_label("En/Decoding Successful. File Saved!")

#  decode button
dec_img = PhotoImage(file="images/decode.png")
decode_img = dec_img.subsample(3, 3)
decode_btn = Button(image=decode_img, highlightthickness=1, command=decode_file)
decode_btn.place(x=250, y=300)


def update_label(status):
    text_label = Label(text=status,
                       font=('Courier', 12, "bold"),
                       fg="white",
                       bg="blue",
                       highlightthickness=0)
    text_label.place(x=260, y=350)

    # show label for X seconds
    if status == "Attempting Decoding..." or status == "En/Decoding Successful. File Saved!":
        window.after(6000, text_label.destroy)
    else:
        window.after(2000, text_label.destroy)

window.mainloop()