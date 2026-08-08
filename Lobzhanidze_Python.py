import tkinter as tk
import re

# 1.Make up an algorithm

def main():

    #The code executed upon submission of input details
    def save_data():
        input_data = input_field.get()
        message.delete("1.0", tk.END)

        # check whether the code contains purely letters or numbers
        if input_data.strip().isalpha():
            #Code executed when htere are alphabetical characters

            if  input_data.strip() == "John":
                message.insert(tk.END, "Hello, John")
                message.tag_add('center','1.0','end') 
                #The input has to match by case
            else:
                message.insert(tk.END, "There is no such name")
                message.tag_add('center','1.0','end')
 
            #checking for a presence of an array/ list; An array containing only separated numbers is accepted
        elif ',' in input_data or ' +' in input_data:
            message.delete("1.0", tk.END)
            try:
                array = [int(i.strip()) for i in re.split(r'[, " + "]', input_data) if i.strip()]
                filtered_array = [i for i in array if i % 3 == 0]
                message.insert(tk.END, f' {str(filtered_array)}\n  Multiples of 3')
                message.tag_add('center','1.0','end')
                #If there are only numbers the code sorts and returns multiples of 3 
            except ValueError:
                message.insert(tk.END, "Enter arrays with numbers separated by commas and/or spaces")
                message.tag_add('center','1.0','end')
                
            #code executed if a single number is entered: Checking if it is greater than 7              
        elif input_data.isnumeric() == True and int(input_data) > 7 :
                message.insert('1.0', "Hello")
                message.tag_add('center','1.0','end')
                       
        input_field.delete(0, tk.END)

        #Button and widget layout done with tkinter
    # root and alignment configuration
    root = tk.Tk()
    root.title('Algorithm Input Screen')
    root.geometry('300x500') 
    center_frame = tk.Frame(root)
    center_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    input_label = tk.Label(center_frame, text="Input Field" , font = ('Helvetica',11))
    input_label.grid(row=2, column=2, pady=4)
    input_field = tk.Entry(center_frame, width=30)
    input_field.grid(row=3, column=2, pady=9)

    submit_button = tk.Button(center_frame, text="Enter", width=13, height=1, font = ('Helvetica',9), command= save_data)
    submit_button.grid(row=4, column=2, pady=10)

    message = tk.Text(center_frame, height=5, width=42)
    message.grid(row=5, column=2, pady=12, padx= 15)
    message.tag_config('center', justify="center")
   

    root.mainloop()

if __name__ == '__main__':
    main()        

    
# 2.  The provided sequence [((())()(())]] is incorrect because closing and opening brackets are not balanced.

# You can replace the second bracket from the left with a square bracket: [[(())()(())]],

# Yoou can replace the second bracket from the right with a parenthesis [( (()) () (()) ) ]

# and you can add a square bracket in the second position from left and at the same time add a parenthesis 
# in the 3rd position from right [[((())()(()))]]













