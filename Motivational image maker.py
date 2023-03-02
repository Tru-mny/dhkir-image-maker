from tkinter import *
import tkinter as tk
from pathlib import Path
import os.path
from PIL import Image, ImageDraw
from PIL import ImageFont

window=tk.Tk()
number = 0


Textbox=tk.Entry(master=window,background="Red",text="Name of image",width=20)
Textbox2=tk.Entry(master=window,background="Green")
Textbox3=tk.Entry(master=window,background="Blue")
labelframe=LabelFrame(window)
left = Label(labelframe)
def imageSaver():
    picinname=Textbox2.get()
    picoutname=Textbox3.get()
    path= "In\{}.png".format(picinname)
    im = Image.open(path)
    W,H = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 40)
    _, _, w, h = draw.textbbox((0, 0), Textbox.get(), font=font)
    #draw.text(((W-w)/2,(H-h)/2), Textbox.get(),font=font, fill="black")
    draw.text(((W-w)/2, (H-h)/2), Textbox.get(), font=font, fill="black")
    im.show()
    im.save("Out\{}.png".format(picoutname), "PNG")


SaveButton=tk.Button(text="To run the command click me!!",                                 
    width=25,
    height=5,
    activebackground="White",
    bg="blue",
    fg="yellow",
    command=imageSaver,
    )   


Textbox3.pack()
Textbox2.pack()
Textbox.pack()
left.pack()
labelframe.pack(fill="both",expand="yes")
SaveButton.pack() 
JournalArea= tk.Text()
JournalArea.pack()
window.mainloop()