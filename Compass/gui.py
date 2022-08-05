#make window
from tkinter import *
tiltCompensatedHeading="start"
window=Tk()
lbl=Label(window, text=tiltCompensatedHeading, bg='black', font=("Helvetica", 1>
window.configure(bg='black')
lbl.pack()
window.title('Hello Python')
window.geometry("300x200+10+10")
                                                                 
def heading():
  with open("Heading.log", "r") as file:
      tiltCompensatedHeading = file.readlines()[-1]
                                                                 
                                                                 
window.after(1,heading)
window.mainloop()
