from tkinter import *
import utils


class Entries:
    all_lis = []
    given_folder_location = ""
    given_file_name = ""
    file_location = ""

    def __init__(self, y):
        self.object_entry = None
        self.y = y

        Entries.all_lis.append(self)

    def create_entry(self, location, size):
        entry = Entry(
            location,
            width=size,
        )
        entry.bind("<Return>", self.when_enter)

        self.object_entry = entry

    def when_enter(self, event):
        print(self.y + 1, end=": ")
        print(self.object_entry.get())
        if self.y == 0:
            Entries.given_folder_location = self.object_entry.get()
            utils.config_dict.update({"folder_location": Entries.given_folder_location})
            utils.json_write()
        if self.y == 1:
            Entries.given_file_name = self.object_entry.get()
            utils.config_dict.update({"file_name": Entries.given_file_name})
            utils.json_write()
        if self.y == 2:
            Entries.file_location = self.object_entry.get()
            utils.config_dict.update({"concat_file_location": Entries.file_location})
            utils.json_write()

    def __repr__(self):
        return f"Entry({self.y + 1})"


class Checkboxes:
    all_checkboxes = []

    def __init__(self, nr, is_checked):
        self.Object_checkbox = None
        self.nr = nr
        self.is_checked = False

        Checkboxes.all_checkboxes.append(self)

    def create_checkbox(self, location, txt, checked):
        checkbox = Checkbutton(
            location,
            text=txt,
            bg="white",
            variable=checked
        )

        #checkbox.bind("<Button-1>", self.check_state)
        self.Object_checkbox = checkbox

    @staticmethod
    def check_state():
        pass

    def __repr__(self):
        return f"Checkbox({self.nr, self.is_checked})"
