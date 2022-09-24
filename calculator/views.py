from tkinter import *
from turtle import width
from typing import Callable

class View:
    def __init__(self):
        # tk() method creates a main window object
        # root variable is having the reference of the main window object. 
        self.root = Tk()
        # StringVar() is a tkinter method
        # The StringVar() helps you manage the value of a widget such as a Label() more effectively.
        # equation var is holding the reference to the StringVar() object
        self.equation = StringVar()

    # this method is used to set the value of Label object by calling set() method from the equation object/StringVar object 
    def set_equation(self, value: str) -> None:
        self.equation.set(value)

    # setup the initial view when application is launched
    # this function takes a "callback" function passed from controller while is is gettingf called from there
    # in this case that callback function is "button_click_handler" function which exist in the controller
    def setup_view(self, callback: Callable) -> None:
        # configuring the main window object
        # initial dimension of window
        self.root.geometry("216x148")
        # disabling resizing of the window
        self.root.resizable(0,0)
        # winow title
        self.root.title("Scalci")
        # window background colour
        self.root.configure(bg="#505050")
        
        # Label() is a tkinter method. 
        # This widget implements a display box where you can place text or images. The text displayed by this widget can be updated at any time you want.
        # syntax => Label(window_object, text/image/content)
        # here, root var has the window object and equation var has the StringVar object 
        calculation = Label(self.root, textvariable=self.equation, width=29, relief="flat", borderwidth=5, bg="#1c1c1c", fg="#ff9500", pady=9)
        # setting initial value to "0"
        self.set_equation("0")
        # setting column span or width
        calculation.grid(columnspan=8)
        # setup_buttons is the instance method function of the View class itself that will help us to render the button on the screen
        # it also utilizes the callback function passed from controller which in trun will be passed to the Button() method by "setup_buttons" function   
        self.setup_buttons(callback)

    def setup_buttons(self, callback: Callable) -> None:
        # rendering the buttons using Button() method
        # Button(window_object, text, (what will happen on button click))
        # also, on every button click it calls the callback function ("button_click_handler" from controller actually) using a lambda function and pass the required argument
        # storing every Button() instance in separate variable 
        button_1 = Button(self.root, width=5, text="1", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("1"))
        button_1.grid(row=1, column=0)

        button_2 = Button(self.root, width=5, text="2", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("2"))
        button_2.grid(row=1, column=1)

        button_3 = Button(self.root, width=5, text="3", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("3"))
        button_3.grid(row=1, column=2)

        button_4 = Button(self.root, width=5, text="4", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("4"))
        button_4.grid(row=2, column=0,)

        button_5 = Button(self.root, width=5, text="5", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("5"))
        button_5.grid(row=2, column=1)

        button_6 = Button(self.root, width=5, text="6", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("6"))
        button_6.grid(row=2, column=2)

        button_7 = Button(self.root, width=5, text="7", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("7"))
        button_7.grid(row=3, column=0,)

        button_8 = Button(self.root, width=5, text="8", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("8"))
        button_8.grid(row=3, column=1)

        button_9 = Button(self.root, width=5, text="9", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("9"))
        button_9.grid(row=3, column=2)

        button_0 = Button(self.root, width=5, text="0", bg="#1c1c1c", fg="#ff9500", command=lambda: callback("0"))
        button_0.grid(row=4, column=0)

        button_plus = Button(self.root, width=10, text="+", bg="#ff9500", command=lambda: callback("+"))
        button_plus.grid(row=1, column=3)

        button_minus = Button(self.root, width=10, text="-", bg="#ff9500", command=lambda: callback("-"))
        button_minus.grid(row=2, column=3)

        button_multi = Button(self.root, width=10, text="x", bg="#ff9500", command=lambda: callback("*"))
        button_multi.grid(row=3, column=3)

        button_divide = Button(self.root, width=10, text="/", bg="#ff9500", command=lambda: callback("/"))
        button_divide.grid(row=4, column=3)

        button_equal = Button(self.root, width=5, text="=", bg="#ff9500", command=lambda: callback("="))
        button_equal.grid(row=4, column=2)

        button_clear = Button(self.root, width=5, text="C", bg="#ff9500", command=lambda: callback("C"))
        button_clear.grid(row=4, column=1)

    
    def start_main_loop(self) -> None:
        # mainloop() is simply a method in the main window object that executes or loop forever until the user exits the window or waits for any events from the user.
        self.root.mainloop()