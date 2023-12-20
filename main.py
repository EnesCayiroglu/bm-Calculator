import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)

def calculate_bmı():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_label.config(text=f"Your bmi: {bmi}")
        except:
            result_label.config(text="Enter a valid number")



#ui
weight_input_label = tkinter.Label(text="Enter your weight (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate",command=calculate_bmı)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

















window.mainloop()