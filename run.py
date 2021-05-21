import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sounddevice as sd
import soundfile as sf
import os
i=0
duration = 10
fs = 44100
questions = ["what is you name?","what is your favourite food?","who are you ?"]

def startrecord():
    myrecording = sd.rec(int(duration * fs),samplerate=fs, channels=2)
    sd.wait()
    return sf.write('./audio/my_Audio_file.flac', myrecording, fs)


def loadquestion():
    i =0
    T = Text(wrapper, height = 5, width = 52)
    T.delete(1.0,END)
    T.insert(1.0, questions.pop(i))
    T.configure(state='disabled')
    T.pack()
    i+=1


root=Tk()

wrapper = LabelFrame(root, text="record your answer here!")
wrapper.pack(fill="both",expand="yes",padx=10,pady=10)


l = Label(wrapper, text = "Question:")
l.config(font =("Courier", 14))
l.pack()


loadquestion()

btn1= Button(wrapper, text="Record", command=startrecord)
btn1.pack(side=tk.LEFT, padx=30, pady=50)

btn1 =Button(wrapper, text="load question", command=loadquestion)
btn1.pack(side=tk.RIGHT, padx=30, pady=50)

root.title("record your answer here!")
root.geometry("500x450")
root.resizable(True,True)
root.mainloop()