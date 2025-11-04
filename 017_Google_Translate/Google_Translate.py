from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = SOR_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")

# Title Label
lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
lab_txt.place(x=50, y=20, height=60, width=400)

# Source Text Label
lab_txt2 = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"))
lab_txt2.place(x=50, y=100, height=30, width=200)

# Source Text Widget
SOR_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
SOR_txt.place(x=50, y=140, height=200, width=400)

# Frame for bottom widgets
frame = Frame(root)
frame.place(x=50, y=360, height=100, width=400)

# Combobox inside frame
list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=0, y=0, height=40, width=120)
comb_sor.set("english")

comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=280, y=0, height=40, width=120)
comb_dest.set("hindi")

# Translate Button
button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=140, y=0, height=40, width=120)

# Destination Text Label
lab_txt3 = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"))
lab_txt3.place(x=50, y=470, height=30, width=250)

# Destination Text Widget
dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=50, y=510, height=150, width=400)

root.mainloop()
