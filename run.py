import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sounddevice as sd
import soundfile as sf
import os
import random 


duration = 10
fs = 44100
root=Tk()

questions = ["what is you name?","what is your favourite food?","who are you ?"]

#### 1. the app load a question randomly from the questions list
def loadquestion():
  
    T = Text(wrapper, height = 5, width = 52)
    T.delete(1.0,END)
    T.insert(1.0, random.choice(questions))
    T.configure(state='disabled')
    T.pack()
### 2. when you hit record button the app will start recording for 10 seconds and saves the file to the same run.py root unter the name my_Audio_file.flac
def startrecord():
    myrecording = sd.rec(int(duration * fs),samplerate=fs, channels=2)
    sd.wait()
    return sf.write('./my_Audio_file.flac', myrecording, fs)

### 3. closes the window when you press quit button
def close_window():
    root.destroy()
    
   
#### Tkinter grafics
####### root ########
wrapper = LabelFrame(root, text="record your answer here!")
wrapper.pack(fill="both",expand="yes",padx=10,pady=10)
####### Question lable ########
l = Label(wrapper, text = "Question:")
l.config(font =("Courier", 14))
l.pack()
loadquestion()

####### recor button ########
btn1= Button(wrapper, text="Record", command=startrecord)
btn1.pack(side=tk.LEFT, padx=50, pady=50)

####### quit button ########
btn2 =Button(wrapper, text= " Quit", command = close_window)
btn2.pack(side=tk.RIGHT, padx=60, pady=50)

root.title("record your answer here!")
root.geometry("350x450")
root.resizable(False,False)
root.mainloop()