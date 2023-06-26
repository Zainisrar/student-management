from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
from PIL import Image, ImageTk
import win32api
import win32print
import time
import tempfile
import datetime
from tkinter.messagebox import showinfo

def installed_printer():
    printers = win32print.EnumPrinters(2)
    for p in printers:
        return(p)

printerdef = ''

def locprinter():
    pt = Toplevel()
##    pt.geometry("250x250")
    pt.title("choose printer")
    var1 = StringVar()
    LABEL = Label(pt, text="Select Printer",bg='goldenrod2',fg='black').pack(fill=X)
    PRCOMBO = ttk.Combobox(pt, width=35)
    print_list = []
    printers = list(win32print.EnumPrinters(2))
    for i in printers:
        print_list.append(i[2])
    print(print_list)
    # Put printers in combobox
    PRCOMBO['values'] = print_list
    defprinter= win32print.GetDefaultPrinter()
    print('Default selected Printer:',defprinter)
    PRCOMBO.set(defprinter)
    PRCOMBO.pack(padx=5,pady=5)
    
    def select():
        global printerdef
        printerdef = PRCOMBO.get()
        pt.destroy()
        print_in_default_printer()
    BUTTON = ttk.Button(pt, text="Print",width=30,command=select).pack(pady=10)
def save_data():



    times = time.strftime("%H:%M:%S")
    dates = time.strftime("%d-%m-%Y")
    current_date = datetime.date.today()

        # Add 5 days to the current date
    payment_within_due_date = current_date + datetime.timedelta(days=10)

        # Convert the new date to the desired format ("%d-%m-%Y")
    due_dates = payment_within_due_date.strftime("%d-%m-%Y")


    payment_after_due_date = payment_within_due_date + datetime.timedelta(days=5)

        # Convert the new date to the desired format ("%d-%m-%Y")
    after_due_dates = payment_after_due_date.strftime("%d-%m-%Y")
    challenge_no = challenge_entry.get()
    name = name_entry.get()
    father_name = father_name_entry.get()
    class_ = class_entry.get()
    section = section_entry.get()
    fees = fees_entry.get()
    try:
        new_fees=int(fees)+100
    except:
        messagebox.showerror("ERROR", "Must be enter data")

    data = f"""
    Excellent Public School
    ------Office Copy----
    Challenge No: {challenge_no}
    Name: {name}
    Father Name: {father_name}
    Class: {class_}
    Section: {section}
    Date: {dates}
    Time: {times}
    Fees: {fees}
    Payment within due Date: {due_dates}
    Payment after due Date: {after_due_dates}
    after due Date Fees: {new_fees}"""
    data1 = f"""
    Excellent Public School
    ------Student Copy----
    Challenge No: {challenge_no}
    Name: {name}
    Father Name: {father_name}
    Class: {class_}
    Section: {section}
    Date: {dates}
    Time: {times}
    Fees: {fees}
    Payment within due Date: {due_dates}
    Payment after due Date: {after_due_dates}"""

    text_display.insert(tk.END, data + "\n")
    text_display.insert(tk.END, data1 + "\n")

    # Clear the entry fields after saving
    challenge_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    father_name_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    section_entry.delete(0, tk.END)
    fees_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    payment_within_due_date_entry.delete(0, tk.END)
    payment_after_due_date_entry.delete(0, tk.END)



root = tk.Tk()
root.geometry("1500x800")
challenge_label = tk.Label(root, text="Challenge No:")
challenge_label.grid(row=0, column=0, padx=5, pady=5)

challenge_entry = tk.Entry(root)
challenge_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=2, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=3, padx=5, pady=5)

father_name_label = tk.Label(root, text="Father Name:")
father_name_label.grid(row=0, column=4, padx=5, pady=5)

father_name_entry = tk.Entry(root)
father_name_entry.grid(row=0, column=5, padx=5, pady=5)

class_label = tk.Label(root, text="Class:")
class_label.grid(row=1, column=0, padx=5, pady=5)

class_entry = tk.Entry(root)
class_entry.grid(row=1, column=1, padx=5, pady=5)

section_label = tk.Label(root, text="Section:")
section_label.grid(row=1, column=2, padx=5, pady=5)

section_entry = tk.Entry(root)
section_entry.grid(row=1, column=3, padx=5, pady=5)

fees_label = tk.Label(root, text="Fees:")
fees_label.grid(row=1, column=4, padx=5, pady=5)

fees_entry = tk.Entry(root)
fees_entry.grid(row=1, column=5, padx=5, pady=5)


submit_button = tk.Button(root, text="Submit", command=save_data)
submit_button.grid(row=11, column=2, columnspan=2, padx=5, pady=10)

text_display = tk.Text(root, height=120, width=200)
text_display.grid(row=13, column=0, columnspan=10, padx=0, pady=0)

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="print", command=locprinter)


def print_in_default_printer():
    printText = text_display.get("1.0", END)
    print(printText)
    print(printerdef)
    
    win32print.SetDefaultPrinter(printerdef)
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(printText)
    # Bellow is call to print text from T2 textbox
    win32api.ShellExecute(
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    showinfo(title='Success',message='Print Successful',detail='Printing is done . thank You!')

root.mainloop()
