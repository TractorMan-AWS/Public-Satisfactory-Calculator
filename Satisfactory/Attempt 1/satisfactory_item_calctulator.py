import json
import os
import tkinter as tk

# Define the directory where your JSON files are located
json_directory = "Satisfactory/Attempt 1/item_data"

def load_item_data(item_name):
    json_file_path = os.path.join(json_directory, f"{item_name}.json")
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        print(f"JSON file not found: {json_file_path}")
        return None

def calculate_result(item_data, required_materials):
    if "Ingredients" in item_data:
        min_items_produced = float('inf')
        for sub_item, sub_quantity in item_data["Ingredients"].items():
            if sub_item not in required_materials:
                return 0
            min_items_produced = min(min_items_produced, required_materials[sub_item] // sub_quantity)
        return min_items_produced * item_data["Result"]
    else:
        return 0

def calculate_required_materials(item_name, required_quantity_per_minute):
    item_data = load_item_data(item_name)
    if item_data:
        required_materials = {}
        for sub_item, rate_per_minute in item_data.get("Ingredients", {}).items():
            required_materials[sub_item] = rate_per_minute * required_quantity_per_minute
        result = calculate_result(item_data, required_materials)
        return required_materials, result
    else:
        return None, None

def calculate_button_clicked():
    item_name = selected_item.get()  # Get the selected item from the dropdown menu
    required_quantity_per_minute = int(quantity_entry.get())
    
    required_materials, result = calculate_required_materials(item_name, required_quantity_per_minute)
    if required_materials and result:
        result_text.config(text=f"Required materials for {item_name} * {required_quantity_per_minute} per minute:")
        material_text.config(text="\n".join([f"{sub_item}: {quantity_per_minute} per minute" for sub_item, quantity_per_minute in required_materials.items()]))
        result_text2.config(text=f"Result: {result} per minute")
    else:
        result_text.config(text=f"No data found for {item_name}")
        result_text2.config(text="")

# Create the main window
window = tk.Tk()
window.title("Satisfactory Calculator")

# Create and configure GUI elements
item_names = [filename.split(".json")[0] for filename in os.listdir(json_directory) if filename.endswith(".json")]
selected_item = tk.StringVar()  # Variable to store the selected item
item_name_label = tk.Label(window, text="Select Item:")
item_name_menu = tk.OptionMenu(window, selected_item, *item_names)
item_name_menu.config(width=20)
quantity_label = tk.Label(window, text="Quantity per Minute:")
quantity_entry = tk.Entry(window)
calculate_button = tk.Button(window, text="Calculate", command=calculate_button_clicked)
result_text = tk.Label(window, text="")
material_text = tk.Label(window, text="")
result_text2 = tk.Label(window, text="")

# Place GUI elements in the window
item_name_label.pack()
item_name_menu.pack()
quantity_label.pack()
quantity_entry.pack()
calculate_button.pack()
result_text.pack()
material_text.pack()
result_text2.pack()

# Start the GUI application
window.mainloop()