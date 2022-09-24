'''
We can use either of the following method.

On the first method => import calculator => all content like Controller(), Model(), View() will be under the name calculator. To use them, calculator.Controller() and so on.

In the second method => from calculator import * => all content like Controller(), Model(), View() will be under their own respective module name. To use them, controllers.Controller(), models.Model() and so on.
'''

# from calculator.controllers import *
# from calculator.views import *
# from calculator.models import *

__all__ = ["controllers", "views", "models"]