import tkinter as tk
import os
import json

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

# Create the main window
window = tk.Tk()
window.title("Ingredient Calculator")
window.geometry("960x540")

# Load the item names from the item_data directory
item_data_folder = os.path.join(os.path.dirname(__file__), "item_data")
item_files = [file.split(".")[0] for file in os.listdir(item_data_folder)]
item_var = tk.StringVar()
item_var.set(item_files[0])

# Create a dropdown for selecting the item
item_label = tk.Label(window, text="Select Item:")
item_dropdown = tk.OptionMenu(window, item_var, *item_files)
item_label.pack()
item_dropdown.pack()

# Create an input field for the required amount
input_label = tk.Label(window, text="Enter Required Amount:")
input_var = tk.Entry(window)
input_label.pack()
input_var.pack()

# Create a button to calculate ingredients
calculate_button = tk.Button(window, text="Calculate Ingredients", command=calculate_ingredients)
calculate_button.pack()

# Create labels to display the result
result_label = tk.Label(window, text="")
result_label.pack()
ingredient_output = tk.Label(window, text="")
ingredient_output.pack()

# Start the GUI event loop
window.mainloop()
