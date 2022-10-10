from tkinter import *
from csvmerger import CsvMerger

class Buttons:
    all_buttons = []

    def __init__(self, y):
        self.object_button = None
        self.y = y

        self.all_buttons.append(self)

    def create_button(self, location):
        button = Button(
            location,
            text="start"
        )
        button.bind("<Button-1>", self.left_click)

        self.object_button = button


    def left_click(self, event):
        CsvMerger.merge()

    def __repr__(self):
        return f"Button({self.y + 1})"