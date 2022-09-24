# import calculator
from calculator import *

# at the start of the application controller is instantiating a controller object which in turn takes the model and view objects as argumets
# View() and Model() is creating the objects of the respective classes on the fly
controller = controllers.Controller(views.View(), models.Model())

# calling "start" function from controller
# entry point of the application
controller.start()