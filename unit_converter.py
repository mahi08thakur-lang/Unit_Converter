import tkinter as tk
from tkinter import ttk, messagebox


def convert():
    try:
        value = float(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    category = category_var.get()
    from_unit = from_var.get()
    to_unit = to_var.get()

    try:
        if category == "Length":
            result = convert_length(value, from_unit, to_unit)

        elif category == "Weight":
            result = convert_weight(value, from_unit, to_unit)

        elif category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)

        elif category == "Time":
            result = convert_time(value, from_unit, to_unit)

        else:
            result = value

        result_label.config(text=f"Result: {result:.4f} {to_unit}")

    except Exception:
        messagebox.showerror("Error", "Conversion failed.")


def convert_length(value, from_unit, to_unit):
    units = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.344,
        "Foot": 0.3048,
        "Inch": 0.0254
    }

    meters = value * units[from_unit]
    return meters / units[to_unit]


def convert_weight(value, from_unit, to_unit):
    units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.45359237,
        "Ounce": 0.0283495
    }

    kilograms = value * units[from_unit]
    return kilograms / units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        celsius = value

    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9

    elif from_unit == "Kelvin":
        celsius = value - 273.15

    if to_unit == "Celsius":
        return celsius

    elif to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32

    elif to_unit == "Kelvin":
        return celsius + 273.15


def convert_time(value, from_unit, to_unit):
    units = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400
    }

    seconds = value * units[from_unit]
    return seconds / units[to_unit]


def update_units(event=None):
    category = category_var.get()

    if category == "Length":
        units = [
            "Meter",
            "Kilometer",
            "Centimeter",
            "Millimeter",
            "Mile",
            "Foot",
            "Inch"
        ]

    elif category == "Weight":
        units = [
            "Kilogram",
            "Gram",
            "Milligram",
            "Pound",
            "Ounce"
        ]

    elif category == "Temperature":
        units = [
            "Celsius",
            "Fahrenheit",
            "Kelvin"
        ]

    elif category == "Time":
        units = [
            "Second",
            "Minute",
            "Hour",
            "Day"
        ]

    from_box["values"] = units
    to_box["values"] = units

    from_box.current(0)
    to_box.current(1 if len(units) > 1 else 0)


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()

window.title("Unit Converter")
window.geometry("500x550")
window.resizable(False, False)


# Title

title = tk.Label(
    window,
    text="UNIT CONVERTER",
    font=("Arial", 24, "bold")
)

title.pack(pady=25)


# Category

category_label = tk.Label(
    window,
    text="Select Category",
    font=("Arial", 12)
)

category_label.pack(pady=5)


category_var = tk.StringVar()

category_box = ttk.Combobox(
    window,
    textvariable=category_var,
    values=[
        "Length",
        "Weight",
        "Temperature",
        "Time"
    ],
    state="readonly",
    width=25
)

category_box.pack(pady=5)

category_box.current(0)

category_box.bind("<<ComboboxSelected>>", update_units)


# Input

entry_label = tk.Label(
    window,
    text="Enter Value",
    font=("Arial", 12)
)

entry_label.pack(pady=(20, 5))


entry = tk.Entry(
    window,
    width=28,
    font=("Arial", 14)
)

entry.pack()


# From Unit

from_label = tk.Label(
    window,
    text="From",
    font=("Arial", 12)
)

from_label.pack(pady=(20, 5))


from_var = tk.StringVar()

from_box = ttk.Combobox(
    window,
    textvariable=from_var,
    state="readonly",
    width=25
)

from_box.pack()


# To Unit

to_label = tk.Label(
    window,
    text="To",
    font=("Arial", 12)
)

to_label.pack(pady=(20, 5))


to_var = tk.StringVar()

to_box = ttk.Combobox(
    window,
    textvariable=to_var,
    state="readonly",
    width=25
)

to_box.pack()


# Buttons

button_frame = tk.Frame(window)

button_frame.pack(pady=25)


convert_button = tk.Button(
    button_frame,
    text="CONVERT",
    width=15,
    font=("Arial", 11, "bold"),
    command=convert
)

convert_button.grid(row=0, column=0, padx=10)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    width=15,
    font=("Arial", 11, "bold"),
    command=clear
)

clear_button.grid(row=0, column=1, padx=10)


# Result

result_label = tk.Label(
    window,
    text="Result: ",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=20)


# Initialize units

update_units()


window.mainloop()