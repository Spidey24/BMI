import tkinter as tk
 
def main():
    def calculate_bmi():
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi_label.config(text="Your BMI is: {:.2f}".format(bmi))
        if bmi < 18.5:
            bmi_status.config(text="Underweight",bg='cyan')
        elif 18.5 <= bmi < 25:
            bmi_status.config(text="Normal weight",bg='green')
        elif 25 <= bmi < 30:
            bmi_status.config(text="Overweight",bg='orange')
        else:
            bmi_status.config(text="Obese",bg='red')

    root = tk.Tk()
    root.title("BMI Calculator")
    root.resizable(False,False)
    root.geometry('500x300')

    # Add an icon to the window
    root.iconbitmap("icon.ico")
    


    weight_label = tk.Label(root, text="Weight (kg)",font=('bold,10'))
    weight_label.place(x=80,y=80)
    weight_label.grid(row=2,column=0)

    weight_entry = tk.Entry(root)
    weight_entry.grid(padx=40,pady=20,row=2, column=1)

    height_label = tk.Label(root, text="Height (m)",font=('bold,10'))
    height_label.grid(padx=50,pady=20,row=3, column=0)

    height_entry = tk.Entry(root)
    height_entry.grid(padx=50,pady=20,row=3, column=1)

    bmi_label = tk.Label(root, text="Your BMI is:",justify="center",font=('bold,10'))
    bmi_label.grid(padx=50,pady=20,row=6, column=0)

    bmi_status = tk.Label(root, text="",justify='center')
    bmi_status.grid(padx=40,pady=20,row=6, column=1)

    calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi,bg='lightgreen')
    calculate_button.grid(row=7, column=0)

    root.mainloop()

if __name__ == '__main__':
    main()