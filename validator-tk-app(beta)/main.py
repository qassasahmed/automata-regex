from tkinter import *
from tkinter import ttk
import validators as v
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)  # for high DPI displays


def on_click():
    if var_option.get() == '1':
        lText.set("Valid") if v.email(eText.get()) else lText.set("Invalid")
    elif var_option.get() == '2':
        lText.set("Valid") if v.password(eText.get()) else lText.set("Invalid")
    elif var_option.get() == '3':
        lText.set("Valid") if v.domain_name(eText.get()) else lText.set("Invalid")
    else:
        lText.set("Please select an option")


def reset_txt():
    eText.set("")
    lText.set("Ready...")  # reset the label
    var_option.set("0")  # reset the radio buttons


root = Tk()
eText = StringVar(root)
lText = StringVar(root)
lText.set("Ready...")
root.configure(padx=50, pady=50)
root.resizable(False, False)
root.title("Validator")
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Entry(frm, width=40, textvariable=eText, font="roboto 14").grid(columnspan=2, row=0, sticky=W)

var_option = StringVar(root, "0")
ttk.Radiobutton(frm, text="email".capitalize(), variable=var_option, value='1').grid(column=0, row=1, sticky=W)
ttk.Radiobutton(frm, text="password".capitalize(), variable=var_option, value='2').grid(column=0, row=2, sticky=W)
ttk.Radiobutton(frm, text="domain name".capitalize(), variable=var_option, value='3').grid(column=0, row=3, sticky=W)

ttk.Button(frm, text="Reset", command=reset_txt).grid(column=1, row=2, sticky=E)
ttk.Button(frm, text="Quit", command=root.destroy, style="Red.TButton").grid(column=1, row=3, sticky=E)
ttk.Button(frm, text="Submit", command=on_click).grid(column=1, row=1, sticky=E)
ttk.Label(frm, textvariable=lText).grid(column=0, row=6, sticky=W)
ttk.Label(frm, text=f"Made with ❤ & ☕ in Matrouh", font="roboto 10 italic").grid(column=1, row=6, sticky=E)

s = ttk.Style()
s.configure('Red.TButton', foreground='#800000')

root.mainloop()
