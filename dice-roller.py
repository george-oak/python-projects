import tkinter
from PIL import Image, ImageTk
import random
import os

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title("George's Dice Roller")

# adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Let's roll some dice!", fg = "blue", font = "Helvetica 16 bold italic")
l1.pack()

# images array
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# construct an empty label widget for image
label1 = tkinter.Label(root, image=None)
label1.image = None

# function that controls everything by button
def rolling_dice():
    script_dir = os.path.dirname(__file__)
    rel_path = "./img/"
    abs_file_path = os.path.join(script_dir, rel_path+random.choice(dice))
    image1 = ImageTk.PhotoImage(Image.open(abs_file_path))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1

# Let's call the function to init
rolling_dice()

label1.pack( expand=True)

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='black', bg='white', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()