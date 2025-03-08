from Converter import converter
from tkinter import *

def convert_text():
    text = text_box.get("1.0",END).strip()
    morse_code = converter(text)
    canvas.itemconfig(text_canvas, text= morse_code)

window = Tk()
window.title("Morse Code Converter")
window.minsize(width=800,height=400)
window.config(bg="black",pady=50)

text_box = Text(bg="white",font="Arial",fg="black")
text_box.config(width=60,height=5,highlightcolor="black",highlightthickness=0)
text_box.grid(column=1,row=1)

canvas = Canvas(width=800,height=200,background="black",highlightthickness=0)
text_canvas = canvas.create_text(400,100,text="Converted Morse Code",width=750,fill="white",
                                  font=("Arial",25,"bold"),justify="center")
canvas.grid(column=1,row=2)


get_button = Button(text="Convert",highlightcolor="white",font=("Arial",25),fg="white",command= lambda : convert_text())
get_button.config(bg="black",highlightthickness=0,width=20)
get_button.grid(column=1,row=3)

window.mainloop()
