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
            text="Concat"
        )
        button.bind("<Button-1>", self.left_click)

        self.object_button = button

    def left_click(self, event):
        CsvMerger.merge()

    def __repr__(self):
        return f"Button({self.y + 1})"


class Listboxes:
    all_listboxes = []

    def __init__(self, y):
        self.object_listbox = None
        self.y = y

        Listboxes.all_listboxes.append(self)

    def create_listbox(self, location):
        listbox = Listbox(
            location,
            width=21
        )
        self.object_listbox = listbox

    @staticmethod
    def show_contents():
        for item in CsvMerger.folder:
            Labels.all_label[0].insert(1, item)

    def __repr__(self):
        return f"Listbox({self.y + 1})"


class Labels:
    all_label = []

    def __init__(self, y):
        self.Object_label = None
        self.y = y

        Labels.all_label.append(self)

    def create_label(self, location, txt):
        label = Label(
            location,
            text=txt,
            bg="white"
        )
        self.Object_label = label



    def __repr__(self):
        return f"Label({self.y + 1})"



