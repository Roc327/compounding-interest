"""

First python app I built from scratch also used to help
learn tkinter.  Simple project to further learning.

"""

# import modules
import tkinter as tk
from tkinter import *


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def calc_interest(principal, interest_rate, time_period, compounding_frequency):
    """ Calculate interest
    """
    amount = principal * (1 +(interest_rate / compounding_frequency)) ** (compounding_frequency * time_period)
    return amount - principal


def on_click():
    """
    Handles the calc_button click event
    """
    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get())
    time_period = float(time_period_entry.get())
    compounding_frequency = float(compounding_frequency_entry.get())

    total_interest = round(calc_interest(principal, interest_rate, time_period, compounding_frequency))
    principal_interest = round(total_interest + principal)

    tot_int_value.config(text=total_interest)
    prin_int_value.config(text=principal_interest)


# create a window
window = Tk()
window.title("Title")
window.update()


w = window.winfo_width()
h = window.winfo_height()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# create widgets
header_label = tk.Label(window, text="Calulate compounding interest.", font=("Arial", 14))
principal_label = tk.Label(window, text="Enter the principal amount:", font=("Arial", 12))
principal_entry = tk.Entry(window)
interest_rate_label = tk.Label(window, text="Enter the interest rate as a decimal:", font=("Arial", 12))
interest_rate_entry = tk.Entry(window)
time_period_label = tk.Label(window, text="Enter the time period in years:", font=("Arial", 12))
time_period_entry = tk.Entry(window)
compounding_frequency_label = tk.Label(window, text="Enter the compounding frequency in years:", font=("Arial", 12))
compounding_frequency_entry = tk.Entry(window)
calc_button = tk.Button(window, text="Calculate", command=on_click)
txt_label = tk.Label(window, text="Your calculated interest is:")
tot_int_txtlabel = tk.Label(window, text="Your total interest is:")
prin_int_txtlabel = tk.Label(window, text="Your principal interest is:")
tot_int_value = tk.Label(window, text="0.00")
prin_int_value = tk.Label(window, text="0.00")

# place widgets into window container
header_label.grid(row=0, column=0, columnspan=3)
principal_label.grid(row=1, column=0)
principal_entry.grid(row=1, column=1, columnspan=2)
interest_rate_label.grid(row=2, column=0)
interest_rate_entry.grid(row=2, column=1, columnspan=2)
time_period_label.grid(row=3, column=0)
time_period_entry.grid(row=3, column=1, columnspan=2)
compounding_frequency_label.grid(row=4, column=0)
compounding_frequency_entry.grid(row=4, column=1, columnspan=2)
txt_label.grid(row=5, column=0, padx=2)
calc_button.grid(row=5, column=1, columnspan=2, padx=2)
tot_int_txtlabel.grid(row=6, column=0, padx=2)
tot_int_value.grid(row=6, column=1, padx=2)
prin_int_txtlabel.grid(row=7, column=0, padx=2)
prin_int_value.grid(row=7, column=1, padx=2)


# center the window
center(window)

# open window
window.mainloop()