from calculator.models import Model
from calculator.views import View

class Controller:
    # here ":" in function argument is just for annotation puposes. python ignores them completely
    # This is a type annotation used by static analysis tools to check, types. It helps ensure program correctness before you run the code.
    # In this case, it is intended as type hint: programs like "mypy" can analyze your code statically (that is, without running it, but only looking at the source code itself) to ensure that only View or Model class type values/objects are passed as arguments to __init__.
    def __init__(self, view: View, model: Model):
        # model holds the object of Model class
        self.model = model
        # view holds the object of View class
        self.view = view

    # gets called at the entry point (just after the controller constructor function) of the application
    def start(self) -> None:
        """Set up and start the view"""
        # calling "setup_view" function from View and passing another function "button_click_handler", a part of controller, to the "setup_view" function
        self.view.setup_view(self.button_click_handler)
        
        # after setting up everything, calling "start_main_loop" method from View.
        # this method calls tkinter internal method "mainloop()" 
        # mainloop() runs parallel to our program and listen to the window object changes simultaneously and allow internal tkinter methods to update it as per the actions performed
        self.view.start_main_loop()

    # button click handler gets triggered from View with a specific argument with respect to the button pressed
    # here we receive the argument and call another set of functions accordingly
    def button_click_handler(self, value: str) -> None:
        """Redirect to the suitable handler function base on the value of the clicked button"""
        if value == "=":
            self._equal_button()
        elif value == "C":
            self._clear_button()
        else:
            self._button_pressed(value)
            
    # when other than = or C pressed
    def _button_pressed(self, num: str) -> None:
        """Add the value of the clicked button to the equation"""
        # first we are getting the value of input_str varable from Model using getter method (data) on the RHS of the assignment operator
        # then append the pressed button value in the present string value of input_str
        # then we are calling setter method (data) and assigning the latest value
        self.model.data += str(num)
        
        # then we are calling set_equation method from View, getting the latest value of input_str variable from Model and then passing it as an argument to the set_equation method
        # set_equation method is responsible to display the actual equation in the object window
        self.view.set_equation(self.model.data)

    # = button pressed
    def _equal_button(self) -> None:
        """Evaluate the equation and show the result"""
        # evaluating the equation
        total = str(eval(self.model.data))
        # then we are calling set_equation method from View and passing the evaluated total as set_equation method is responsible to display the actual equation in the object window
        # basically showing the result
        self.view.set_equation(total)
        # after displaying the result, we are calling setter method (data) from Model and re-assigning the input_str variable value to "" (empty)
        self.model.data = ""

    # C button pressed
    def _clear_button(self) -> None:
        """Clear out the sreen of the calculator"""
        # we are calling setter method (data) from Model and assigning the value to "" (empty)
        self.model.data = ""
        # calling set_equation from View, also getting input_str variable value from Model and passing it to the set_equation method for updating the equation display which is "" (empty) 
        self.view.set_equation(self.model.data)