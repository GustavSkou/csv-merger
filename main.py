import utils
from tkinter import *

from widgets import Buttons
from widgets import Listboxes
from widgets import Labels
from entrieswidgets import Checkboxes
from entrieswidgets import Entries


win = Tk()
win.configure(bg="white")
win.geometry(f"{utils.width}x{utils.height}")
win.resizable(False, False)
win.title("csv merger")

left_frame = Frame(
    win,
    bg="white",
    width=utils.width * 0.7,
    height=utils.height
)

right_frame = Frame(
    win,
    bg="gray",
    width=utils.width * 0.3,
    height=utils.height
)

left_frame.place(x=0, y=0)
right_frame.place(x=utils.width * 0.7, y=0)


# Creating objects and placeing them
for y in range(3):                  # Entry 1-3
    e = Entries(y=y)
    e.create_entry(
        location=left_frame,
        size=30
    )
    txt = utils.json_read(utils.config_entries_keys[y])
    e.object_entry.insert(
        0, txt
    )
    e.object_entry.place(
        x=130, y=30+y*45
    )

for y in range(1):                  # Button 1
    b = Buttons(y=y)
    b.create_button(
        location=left_frame
    )
    b.object_button.place(
        x=35, y=165
    )

lb = Listboxes(y=0)                  # Listbox 1
lb.create_listbox(
    location=right_frame
)
lb.object_listbox.place(
    x=10, y=30
)

txt = {0: "Folder location", 1: "New file name", 2: "New file location"}
for y in range(3):                      # Label
    l = Labels(y=y)
    l.create_label(
        location=left_frame,
        txt=txt[y]
    )
    l.Object_label.place(
        x=30, y=28+y*45
    )

ctxt = {0: "Index", 1: "Header"}        # Checkbox 1, 2

for nr in range(2):
    var = utils.json_read(utils.config_checkbuttons_keys[nr])
    if var == 1:
        var = True
    else:
        var = False
    cb = Checkboxes(nr=nr, is_checked=var)
    cb.create_checkbox(
        location=left_frame,
        txt=ctxt[nr],
        checked=utils.json_read(utils.config_checkbuttons_keys[nr])
    )
    cb.Object_checkbox.place(
        x=125, y=160+nr*30
    )
    if utils.json_read(utils.config_checkbuttons_keys[nr]) == 1:
        cb.Object_checkbox.select()

print(Entries.all_lis)
print(Buttons.all_buttons)
print(Listboxes.all_listboxes)
print(Checkboxes.all_checkboxes)

win.mainloop()
