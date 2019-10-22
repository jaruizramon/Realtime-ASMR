# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:44:20 2019

@author: Pipo
"""

from tkinter import Tk, Label, Button
import relez

class RelezGUI:
    
    def __init__(self, master):
        
        self.master = master
        master.title("Relexperience")

        self.label = Label(master, text="Press 'RUN' to relax.")
        self.label.pack()

        self.greet_button = Button(master, text="RUN", command=relez.main)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


root = Tk()
my_gui = RelezGUI(root)
root.mainloop()