from tkinter import *


class Entries:
    all_lis = []
    given_folder_location = ""
    given_file_name = ""

    def __init__(self, y):
        self.object_entry = None
        self.y = y

        Entries.all_lis.append(self)

    def create_entry(self, location):
        entry = Entry(
            location,
            width=20,
        )
        entry.bind("<Return>", self.when_enter)

        self.object_entry = entry


    def when_enter(self, event):
        print(self.y + 1, end=": ")
        print(self.object_entry.get())
        if self.y == 0:
            Entries.given_folder_location = self.object_entry.get()
        if self.y == 1:
            Entries.given_file_name = self.object_entry.get()


    def __repr__(self):
        return f"Entry({self.y + 1})"
