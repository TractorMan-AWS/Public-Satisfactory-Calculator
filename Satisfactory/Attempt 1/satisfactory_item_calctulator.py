from tkinter import *
import os
import json

# Create the main window
window = Tk()
window.title("Ingredient Calculator")
window.iconbitmap('Testing_Grounds_PY/Satisfactory/Images/icon/cha0scharly.ico')
window.geometry("417x950")

# Menu frame
menu_frame = LabelFrame(window, pady=5)
menu_frame.grid(row=0, column=0, columnspan=2, sticky=W)

# Exit Button
file=Button(menu_frame, text="File", padx=10, pady=1, fg="#e49245", bg="#4c5b5f")
file.grid(row=0, column=0)

# Edit
edit=Button(menu_frame, text="Edit", padx=10, pady=1, fg="#e49245", bg="#4c5b5f")
edit.grid(row=0, column=1)

# Options
options=Button(menu_frame, text="Options", padx=10, pady=1, fg="#e49245", bg="#4c5b5f")
options.grid(row=0, column=2)

#Spare
save=Button(menu_frame, text="Save", padx=10, pady=1, fg="#e49245", bg="#4c5b5f")
save.grid(row=0, column=3)

# Exit
exit = Button(menu_frame, text="Exit", command=window.quit, padx=10, pady=1, fg="#e49245", bg="#4c5b5f")
exit.grid(row=0, column=4)

# Frame 1
frame1 = LabelFrame(window, text="Item Calculator", fg="#e49245", bg="#4c5b5f")
frame1.grid(row=1, column=0)

# Function to calculate required ingredients
def calculate_ingredients():
    try:
        item_name = item_var.get()
        required_amount = float(input_var.get())
        
        # Build the full path to the "item_data" folder
        item_data_folder = os.path.join(os.path.dirname(__file__), "item_data")

        with open(os.path.join(item_data_folder, f'{item_name}.json')) as file:
            item_data = json.load(file)
        
        result = item_data[item_name]["Result"]
        ingredients = item_data[item_name]["Ingredients"]
        
        required_ingredients = {ingredient: required_amount / result * amount for ingredient, amount in ingredients.items()}
        
        formatted_output = "\n".join([f"{ingredient}: {amount}" for ingredient, amount in required_ingredients.items()])
        ingredient_output.config(text=formatted_output)
    except (ValueError, FileNotFoundError, KeyError):
        result_label.config(text="Invalid item or input.")

# Load the item names from the item_data directory
item_data_folder = os.path.join(os.path.dirname(__file__), "item_data")
item_files = [file.split(".")[0] for file in os.listdir(item_data_folder)]
item_var = StringVar()
item_var.set(item_files[0])

# Create a dropdown for selecting the item
item_label = Label(frame1, text="Select Item:", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
item_dropdown = OptionMenu(frame1, item_var, *item_files)
item_label.pack()
item_dropdown.pack()
item_dropdown.config(fg="#e49245", bg="#4c5b5f")
item_dropdown["menu"].config(fg="#e49245", bg="#4c5b5f")

# Create an input field for the required amount
input_label = Label(frame1, text="Enter Required Amount:", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
input_var = Entry(frame1, fg="#e49245", bg="#4c5b5f",)
input_label.pack()
input_var.pack()

# Create a button to calculate ingredients
calculate_button = Button(frame1, padx=10, pady=1, text="🔻Calculate Ingredients🔻", command=calculate_ingredients, fg="#e49245", bg="#4c5b5f")
calculate_button.pack()

# Create labels to display the result
result_label = Label(frame1, text="", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
result_label.pack()
ingredient_output = Label(frame1, text="", fg="#e49245", bg="#4c5b5f", padx=10, pady=1)
ingredient_output.pack()

# Exporting to Text
def export():
    global ingredient_output
    global frame3
    ingredient_output = e.get()
    note = Text(frame3, height=25, width=50, borderwidth=5, fg="#e49245", bg="#4c5b5f")
    note.grid(row=0, column=0, columnspan=4)


# Export of Results
button_export = Button(frame1, text="🔻Export To Notes🔻", command=export, fg="#e49245", bg="#4c5b5f")
button_export.pack()


# Frame 2
frame2 = LabelFrame(window, text="Standard Calculator", fg="#e49245", bg="#4c5b5f")
frame2.grid(row=1, column=1)

#Calculator
e = Entry(frame2, width=30, borderwidth=5, fg="#e49245", bg="#4c5b5f")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Number Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Clear Entry
def button_ce():
    e.delete(0, END)

# Addition Function
def button_plus():
    first_number = e.get()
    global f_num 
    global math 
    math = "plus"
    f_num = int(first_number)
    e.delete(0, END)

# Subtraction Function
def button_minus():
    first_number = e.get()
    global f_num 
    global math 
    math = "minus"
    f_num = int(first_number)
    e.delete(0, END)

# Muntiplcation Function
def button_times():
    first_number = e.get()
    global f_num 
    global math 
    math = "times"
    f_num = int(first_number)
    e.delete(0, END)

#Divition Function
def button_divide():
    first_number = e.get()
    global f_num 
    global math 
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

# Output Result
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "plus":
        e.insert(0, f_num + int(second_number))

    if math == "minus":
        e.insert(0, f_num - int(second_number))

    if math == "times":
        e.insert(0, f_num * int(second_number))

    if math == "divide":
        e.insert(0, f_num / int(second_number))



# Define layout
button_1 = Button(frame2, text="1", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(1))
button_2 = Button(frame2, text="2", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(2))
button_3 = Button(frame2, text="3", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(3))
button_4 = Button(frame2, text="4", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(4))
button_5 = Button(frame2, text="5", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(5))
button_6 = Button(frame2, text="6", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(6))
button_7 = Button(frame2, text="7", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(7))
button_8 = Button(frame2, text="8", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(8))
button_9 = Button(frame2, text="9", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(9))
button_0 = Button(frame2, text="0", padx=20, pady=10, fg="#e49245", bg="#4c5b5f", command=lambda: button_click(0))
button_plus = Button(frame2, text="+", padx=17, pady=10, fg="#e49245", bg="#4c5b5f", command= button_plus)
button_equal = Button(frame2, text="=", padx=100, pady=10, fg="#e49245", bg="#4c5b5f", command=button_equal)
button_clear = Button(frame2, text="Clear", padx=37, pady=10, fg="#e49245", bg="#4c5b5f", command=button_ce)

button_minus = Button(frame2, text="-", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_minus)
button_times = Button(frame2, text="*", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_times)
button_divide = Button(frame2, text="/", padx=19, pady=10, fg="#e49245", bg="#4c5b5f", command= button_divide)

# Button Layout

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0,)

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=0, columnspan=4)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_times.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# Frame 3
frame3 = LabelFrame(window, text="Notes")
frame3.grid(row=2, column=0, columnspan=2)

note = Text(frame3, fg="#e49245", bg="#4c5b5f", width=50)
note.grid(row=0, column=0, columnspan=4)

# Start the GUI event loop
window.mainloop()
