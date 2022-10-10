import settings
from tkinter import *
from entrys import Entries
from button import Buttons


win = Tk()
win.configure(bg="white")                              # bg = background
win.geometry(f"{settings.width}x{settings.height}")    # The size
win.resizable(False, False)
win.title("csv merger")

left_frame = Frame(
    win,
    bg="red",
    width=settings.width * 0.3,
    height=settings.height
)

right_frame = Frame(
    win,
    bg="blue",
    width=settings.width * 0.7,
    height=settings.height
)

left_frame.place(x=0, y=0)
right_frame.place(x=settings.width * 0.3, y=0)


for y in range(3):
    e = Entries(y=y)
    e.create_entry(
        location=right_frame
    )
    e.object_entry.place(
        x=75, y=30+y*45
    )

for y in range(1):
    b = Buttons(y=y)
    b.create_button(
        location=left_frame
    )
    b.object_button.place(
        x=40, y=30+y*45
    )

print(Entries.all_lis)
print(Buttons.all_buttons)

win.mainloop()
