from tkinter import *
import tkinter as tk
from pathlib import Path
import os.path#useless but i still kept cause i can mwahahaha
from PIL import Image, ImageDraw
from PIL import ImageFont
import arabic_reshaper #for the bad way pyhton ineracts with arabic
from bidi.algorithm import get_display #for the bad way the previous library inverst the text when resolved
import random
from instabot import Bot
from instagrapi import Client
import os 
import glob
from PIL import Image


#cookie_del = glob.glob("config/*cookie.json")
#os.remove(cookie_del[0])

window=tk.Tk()
number = 0

Textbox=tk.Entry(master=window,background="Red",text="Name of image",width=20)
Textbox2=tk.Entry(master=window,background="Green")
Textbox3=tk.Entry(master=window,background="Blue")
labelframe=LabelFrame(window)
left = Label(labelframe)


global reshaped_text #to be able to use the variable in the other formulas
bidi_text=0
def randomer(): #this is basically a way to choose line at random that fits in the image
    x1=random.randint(1,195)
    global bidi_text
    textget = open("Dhikr.txt",encoding='utf-8')
    text_to_be_reshaped = textget.readlines()[x1]
    if len(text_to_be_reshaped)<30:
        reshaped_text = arabic_reshaper.reshape(str(text_to_be_reshaped))
        bidi_text = get_display(reshaped_text)
        print(bidi_text)
    else:
        randomer()        
    






def imageSaver():
    randomer()
    global bidi_text
    #picinname=Textbox2.get()
    picoutname=Textbox3.get()
    path= "In\Image.jpg"
    im = Image.open(path)
    W,H = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 90)
    _, _, w, h = draw.textbbox((0, 0), bidi_text, font=font)
    #draw.text(((W-w)/2,(H-h)/2), Textbox.get(),font=font, fill="black")
    draw.text(((W-w)/2, (H-h)/2), bidi_text, font=font, fill="White")
    im.show()
    im.save("Out\hh.jpeg")
    


SaveButton=tk.Button(text="To run the command click me!!",                                 
    width=25,
    height=5,
    activebackground="White",
    bg="blue",
    fg="yellow",
    command=imageSaver,
    )   

#def poster():
 #   cl =Client()
 #
 #   cl.login(username = "dhikrbot",
 #         password = "Naser2004")
 #   media = cl.photo_upload(path="Out\hh.jpeg",
 #                caption ="#islamic #islam #allah #muslim #islamicquotes #quran #muslimah #allahuakbar #deen #dua #makkah #islamicpost #islamicreminders #sunnah #ramadan #prophetmuhammad #hijab #love #alhamdulillah #muhammad #islamicreminder #muslims #jannah #instagram #islamicart #namaz #madinah #madina #pakistan #islamicquote")

def UPhoto():
    bot = Bot()
    bot.login(username = "dhikrbot", password="Naser2004")
    bot.upload_photo('Out\hh.jpeg', caption=("#islamic #islam #allah #muslim #islamicquotes #quran #muslimah #allahuakbar #deen #dua #makkah #islamicpost #islamicreminders #sunnah #ramadan #prophetmuhammad #hijab #love #alhamdulillah #muhammad #islamicreminder #muslims #jannah #instagram #islamicart #namaz #madinah #madina #pakistan #islamicquote"))

postButton=tk.Button(text="I post!!!!",                                 
    width=25,
    height=5,
    activebackground="White",
    bg="blue",
    fg="yellow",
    command=UPhoto,
    )   

postButton.pack()
Textbox3.pack()
#Textbox2.pack()
Textbox.pack()
left.pack()
labelframe.pack(fill="both",expand="yes")
SaveButton.pack() 
JournalArea= tk.Text()
JournalArea.pack()
window.mainloop()