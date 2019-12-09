
class VariableObject(object):

    def __init__(self):
        # This will hold the python exec string for the variable declaration
        self.exex_string = ""

    # Turns language variable into python variable for execution in python
    def transpile(self, name, operator, value):
        # Appends the python executable string converted using out parser
        self.exex_string += name + " " + operator + " " + value + "\n"

        # Return exec_string which holds put python varibale we created
        return self.exex_string