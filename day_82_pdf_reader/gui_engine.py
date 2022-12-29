from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window = Tk()
window.title("PDF2Audio")

# currently working on desktop version of the app

BACKGROUND_COLOR = "#4696e5"

window.minsize(width=600, height=300)
window.resizable(False, False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=600, height=280)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(460, 50, text="OceanReader", font=("Ariel", 40, "bold"))
canvas.create_text(388, 85, text="Save Time! Upload your Book | Download as Audio!", font=("Ariel", 16, "bold"))
canvas.create_text(403, 105, text="I'll read it for you, while you go about your day!", font=("Ariel", 16, "bold"))

def select_file():
    filetypes = (
        ('pdf files', '*.pdf')
    )

    filename = fd.askopenfilename(
        title='Open a PDF with Text',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
# open button
upload_button = ttk.Button(
    window,
    text='Upload PDF',
    command=select_file
)

upload_button.grid(column=1, row=1, columnspan=2)

window.mainloop()