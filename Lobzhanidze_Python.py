import tkinter as tk
import time
import re

# 1.Make up an algorithm


#The algorithm executed upon submission of input details
def save_data():
  
    input_data = input_field.get()
    time.sleep(1)
    message.delete("1.0", tk.END)

    # check whether the code contains purely letters or numbers

    if input_data.isalpha() == True:
        #Code executed when htere are alphabetical characters

        if "John" in input_data:
            message.insert(tk.END, "Hello, John") 
            #The input is checked for case
        else:
            message.insert(tk.END, "There is no such name")

           
    #checking for a presence of an array/ list; An array containing only separated numbers is accepted
    if ',' in input_data or ' +' in input_data:
        message.delete("1.0", tk.END)
        try:
            array = [int(i.strip()) for i in re.split(r'[, " + "]', input_data) if i.strip()]
            filtered_array = [i for i in array if i % 3 == 0]
            message.insert(tk.END, f'{  str(filtered_array)}\n Multiples of 3')
            #If there are only nummber the code sorts and returns multiples of 3 
        except ValueError:
            message.insert(tk.END, "Enter arrays with numbers separated by commas and/or spaces")

    #code executed if a single number is entered: Checking if it is greater than 7 or not              
    if input_data.isnumeric() == True:
        num = int(input_data)
        if num > 7:
            message.insert('1.0', "Hello")
        else:
            pass
            
    input_field.delete(0, tk.END)

#Button and widget layout done with tkinter
root = tk.Tk()
root.title('Algorithm Input Page')
root.geometry('300x500') 

center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

input_label = tk.Label(center_frame, text="Input Field").grid(row=2, column=2, pady=4)
input_field = tk.Entry(center_frame, width=30)
input_field.grid(row=3, column=2, pady=9)

submit_button = tk.Button(center_frame, text="Enter", width=13, height=1, command= save_data)
submit_button.grid(row=4, column=2, pady=10)

message = tk.Text(center_frame, height=3, width=40)
message.grid(row=5, column=2, pady=12, padx= 15)

root.mainloop()


    
# 2.  The provided sequence [((())()(())]] is incorrect because closing and opening brackets are not balanced.

# You can replace the second bracket from the left with a square bracket: [[(())()(())]],

# Yoou can replace the second bracket from the right with a parenthesis [( (()) () (()) ) ]

# and you can add a square bracket in the second position from left and at the same time add a parenthesis 
# in the 3rd position from right [[((())()(()))]]













