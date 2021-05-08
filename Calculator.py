import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Calculator")
root.geometry("675x150")
root.configure(bg="cyan")

# Definitions
def enter_button():
	numbers = user_input.get()
	if numbers[1] == "+":
		first_number = numbers[0]
		operator = numbers[1]
		last_number = numbers[2]
		first_number_int = int(first_number)
		last_number_int = int(last_number)

		calculation_plus = first_number_int + last_number_int
		user_input.insert(tkinter.END, f" = {calculation_plus}")

	if numbers[1] == "-":
		first_number = numbers[0]
		operator = numbers[1]
		last_number = numbers[2]
		first_number_int = int(first_number)
		last_number_int = int(last_number)

		calculation_plus = first_number_int - last_number_int
		user_input.insert(tkinter.END, f" = {calculation_plus}")

	if numbers[1] == "/":
		first_number = numbers[0]
		operator = numbers[1]
		last_number = numbers[2]
		first_number_int = int(first_number)
		last_number_int = int(last_number)

		calculation_plus = first_number_int / last_number_int
		user_input.insert(tkinter.END, f" = {calculation_plus}")

	if numbers[1] == "X":
		first_number = numbers[0]
		operator = numbers[1]
		last_number = numbers[2]
		first_number_int = int(first_number)
		last_number_int = int(last_number)

		calculation_plus = first_number_int * last_number_int
		user_input.insert(tkinter.END, f" = {calculation_plus}")
	

# Creating GUI things
user_input = Entry(root, width=70, bg="gray")
user_input.pack(side="bottom")

one_btn = Button(root, text="1", command=lambda: user_input.insert(tkinter.END,"1"))
one_btn.pack(side="left")

two_btn = Button(root, text="2", command=lambda: user_input.insert(tkinter.END,"2"))
two_btn.pack(side="left")

three_btn = Button(root, text="3", command=lambda: user_input.insert(tkinter.END,"3"))
three_btn.pack(side="left")

four_btn = Button(root, text="4", command=lambda: user_input.insert(tkinter.END,"4"))
four_btn.pack(side="left")

five_btn = Button(root, text="5", command=lambda: user_input.insert(tkinter.END,"5"))
five_btn.pack(side="left")

six_btn = Button(root, text="6", command=lambda: user_input.insert(tkinter.END,"6"))
six_btn.pack(side="left")

seven_btn = Button(root, text="7", command=lambda: user_input.insert(tkinter.END,"7"))
seven_btn.pack(side="left")

eight_btn = Button(root, text="8", command=lambda: user_input.insert(tkinter.END,"8"))
eight_btn.pack(side="left")

nine_btn = Button(root, text="9", command=lambda: user_input.insert(tkinter.END,"9"))
nine_btn.pack(side="left")

plus_btn = Button(root, text="+", command=lambda: user_input.insert(tkinter.END,"+"))
plus_btn.pack(side="left")

minus_btn = Button(root, text="-", command=lambda: user_input.insert(tkinter.END,"-"))
minus_btn.pack(side="left")

times_btn = Button(root, text="X", command=lambda: user_input.insert(tkinter.END,"X"))
times_btn.pack(side="left")

divide_btn = Button(root, text="/", command=lambda: user_input.insert(tkinter.END,"/"))
divide_btn.pack(side="left")

enter_btn = Button(root, text="ENTER", command=enter_button)
enter_btn.pack(side="left")

clear_btn = Button(root, text="CLEAR", command=lambda: user_input.delete(0, END))
clear_btn.pack(side="left")

# Configs
one_btn.configure(height=5, width=5)

two_btn.configure(height=5, width=5)

three_btn.configure(height=5, width=5)

four_btn.configure(height=5, width=5)

five_btn.configure(height=5, width=5)

six_btn.configure(height=5, width=5)

seven_btn.configure(height=5, width=5)

eight_btn.configure(height=5, width=5)

nine_btn.configure(height=5, width=5)

plus_btn.configure(height=5, width=5)

minus_btn.configure(height=5, width=5)

times_btn.configure(height=5, width=5)

divide_btn.configure(height=5, width=5)

enter_btn.configure(height=5, width=5)

clear_btn.configure(height=5, width=5)

root.mainloop()