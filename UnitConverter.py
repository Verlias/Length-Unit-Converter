import tkinter as tk

def convert():
    input_unit = input_unit_var.get()
    output_unit = output_unit_var.get()
    value = float(entry_input.get("1.0", tk.END))

    # Define conversion factors
    conversion_factors = {
        "Meters(m)": 1,
        "Centimeters(cm)": 100,
        "Millimeter(mm)": 1000,
        "Kilometers(km)": 0.001,
        "Inches(in)": 39.3701,
        "Feet(ft)": 3.28084,
        "Yards(yd)": 1.09361,
        "Miles(mi)": 0.000621371,
    }

    # Convert input value to meters
    meters_value = value / conversion_factors[input_unit]

    # Convert meters to output unit
    result = meters_value * conversion_factors[output_unit]

    entry_output.delete("1.0", tk.END)
    entry_output.insert("1.0", str(result))

# Create main window 
root = tk.Tk()
root.title("Unit Converter")
root.geometry("450x250")

# Available units
options = [
    "Meters(m)",
    "Centimeters(cm)",
    "Millimeter(mm)",
    "Kilometers(km)",
    "Inches(in)",
    "Feet(ft)",
    "Yards(yd)",
    "Miles(mi)",
]

# Input
label_input = tk.Label(root, text="Input Value:")
label_input.pack()
entry_input = tk.Text(root, height=1, width=40)
entry_input.pack(pady=5)

# Input unit dropdown
label_input_unit = tk.Label(root, text="From:")
label_input_unit.pack()
input_unit_var = tk.StringVar(root)
input_unit_dropdown = tk.OptionMenu(root, input_unit_var, *options)
input_unit_dropdown.pack()

# Output unit dropdown
label_output_unit = tk.Label(root, text="To:")
label_output_unit.pack()
output_unit_var = tk.StringVar(root)
output_unit_dropdown = tk.OptionMenu(root, output_unit_var, *options)
output_unit_dropdown.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Output
label_output = tk.Label(root, text="Converted Value:")
label_output.pack()
entry_output = tk.Text(root, height=1, width=40)
entry_output.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
