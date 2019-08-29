#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import fasttext


global model

def predict(text):
    predict = model.predict(text, 3)
    genres = []
    for i,p in enumerate(predict[1]):
            if(p > 0.140):
                genres.append(predict[0][i][9:])
    result = ", ".join(genres)
    return result

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("IMDb genre classification")
        self.minsize(480, 480)
        
        self.parent = ttk.Frame(self)
  
        self.buttonR()
        self.text = ScrolledText(self.parent)
        self.text.grid(column = 0, row = 2, ipady = 3)
        self.labelR = ttk.Label(self.parent, text = "")
        self.labelR.grid(column = 0, row = 3)         
        self.parent.pack(expand = 1)
  
    def buttonR(self):
        self.buttonR = ttk.Button(self.parent, text = "Predict", command = self.predict)
        self.buttonR.grid(column = 0, row = 1)

    def predict(self):
        self.result = predict(self.text.get('1.0', END+'-1c'))
        #self.labelR = ttk.Label(self, text = "")
        #self.labelR.grid(column = 0, row = 5)
        self.labelR.configure(text = self.result)


# load model
model = fasttext.load_model('model.ftz')
 
root = Root()
root.mainloop()