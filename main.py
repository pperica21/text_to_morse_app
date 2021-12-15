from tkinter import *
from PIL import ImageTk, Image
from morse_converter import text_to_morse

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MorseConverter")
window.geometry("400x400")
window.minsize(600, 600)
window.maxsize(600, 600)
window.config(bg="white", padx=100, pady=100)


title_img = ImageTk.PhotoImage(Image.open("TextToMorse-title_text.png"))
title_img_lbl = Label(window, image=title_img, bg="white").place(x=-150, y=-110)

text_box_img = ImageTk.PhotoImage(Image.open("text_box_pic.png"))
text_box_lbl = Label(window, image=text_box_img, bg="white").place(x=-48, y=20)
user_entry = Text(window, font=("Georgia", 15), width=30, height=3.4)
user_entry.place(x=19, y=114)


def get_user_input():
    """ Takes users input and runs it trough text_to_morse function"""
    user_input = user_entry.get("1.0", "end-1c")
    text_to_morse(user_input=user_input)


button_image = ImageTk.PhotoImage(Image.open("button_pic.png"))
convert_button = Button(window, image=button_image, borderwidth=0, bg="white",
                        command=get_user_input).place(x=47, y=270)


window.mainloop()
