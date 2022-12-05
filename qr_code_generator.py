#-------------------------------------------------------------------------------
# Name:        QR CODE GENERATOR
# Purpose:     Education
#
# Author:      rnicolescu
#
# Created:     3/12/2022
# Copyright:   (c) nicol 2022
# Licence:     <HOME>
#-------------------------------------------------------------------------------

from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

# CONSTANTS
font_settings = ("Arial", 12, "bold")
background_colour = "white"

# -------------------------- QR CODE GENERATOR ------------------------- #
def generator():

    url_address = qr_entry.get()

    url = pyqrcode.create(url_address)

    url.png(name_entry.get() + ".png", scale=8, module_color=[0, 0, 0, 128])


def clear_fields():

    qr_entry.delete(0, END)
    name_entry.delete(0, END)

# -------------------------- GUI SETUP ------------------------- #

window = Tk()
window.title("QR-code-generator v1.0")
window.config(padx=20, pady=20, bg="white")
window.geometry("700x450")

# Canvas
canvas = Canvas(width=400, height=227, highlightthickness=0)
photo = ImageTk.PhotoImage(file="logo.jpeg")
canvas.create_image(200,114, image=photo)
canvas.grid(row=0, column=1, columnspan=2)

# Labels and Buttons
empty_row = Label()
empty_row.grid(row=1, column=0)

qr_generator = Label(text="URL:", font=font_settings, background=background_colour)
qr_generator.grid(row=2, column=0)

qr_entry = Entry(width=100)
qr_entry.grid(row=2, column=1)
qr_entry.focus()

name_qr = Label(text="Name:", font=font_settings, background=background_colour)
name_qr.grid(row=3, column=0)
name_entry = Entry(width=100)
name_entry.grid(row=3, column=1)


generate = Button(text="Generate\nQR CODE!",font=font_settings, background=background_colour, command=generator)
generate.grid(row=5, column=1)

clear_button = Button(text="Clear\n fields!", font=font_settings, background=background_colour, command=clear_fields)
clear_button.grid(row=6, column=1)


mainloop()
