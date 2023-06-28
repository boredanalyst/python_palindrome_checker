from tkinter import *
from tkinter import ttk

## Setting up the functions.

def checkPalindrome():
    ## verify if entry text has a value.

    if ent_input.get() == "": 
        lbl_result.config(text="Please provide a text to check.")
        return

    text_to_check = ent_input.get()

    text_to_check = text_to_check.upper()

    reversed = ""

    ##for letter in text_to_check:
      ##  reversed += letter

    for letter in range(len(text_to_check) - 1, -1,-1):
        reversed += text_to_check[letter]
        lbl_result.config(text=reversed)
    
    ## check for palindrome

    if reversed == text_to_check:
      lbl_result.config(text="It's a palindrome.")
    else:
      lbl_result.config(text="Not a palindrome.")


## Setting up the main window.

root = Tk()
root.geometry("300x300")
root.title("Palindrome Checker")

lbl_title = ttk.Label(root,text="Palindrome Checker",font=(12),background="skyblue",anchor="w")
lbl_title.pack(padx=3,pady=3,fill=BOTH)

## Input fields.

frm_input = ttk.Frame(root,relief=GROOVE,padding=4)
frm_input.pack(padx=3,pady=3,fill=BOTH)

lbl_input = ttk.Label(frm_input,text="Provide your text",anchor="w")
lbl_input.pack(padx=3,pady=3,fill=BOTH)

ent_input = ttk.Entry(frm_input,width=30)
ent_input.pack(padx=3,pady=3,fill=BOTH)

btn_check = ttk.Button(frm_input,text="Check",command=checkPalindrome)
btn_check.pack(padx=3,pady=3,fill=BOTH)

lbl_result = ttk.Label(frm_input,text="",anchor="w")
lbl_result.pack(padx=3,pady=3,fill=BOTH)

root.mainloop()