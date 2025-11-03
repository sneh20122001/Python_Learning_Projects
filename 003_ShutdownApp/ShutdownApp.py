from tkinter import *
import os 

st = Tk()

st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="blue")

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")


r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"), 
                  relief=RAISED, cursor="plus",command=restart)
r_button.place(x=180, y=60, height=50, width=150)

rt_button = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"), 
                   relief=RAISED, cursor="plus",command=restart_time)
rt_button.place(x=180, y=160, height=50, width=170)

lg_button = Button(st, text="Log-out", font=("Times New Roman", 20, "bold"), 
                   relief=RAISED, cursor="plus",command=logout)
lg_button.place(x=180, y=260, height=50, width=150)

st_button = Button(st, text="Shutdown", font=("Times New Roman", 20, "bold"), 
                   relief=RAISED, cursor="plus",command=shutdown)
st_button.place(x=180, y=360, height=50, width=150)

st.mainloop()
