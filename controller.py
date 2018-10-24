class Controller:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operators = ["+", "-", "*", "/", "+/-", "."]
    cancellers = ["CE", "C", "Del"]

    def __init__(self, model):
        self.model = model
        self.operand1 = "0"
        self.operand2 = ""
        self.operator = ""
    
    def calculate(self):
            if self.operand2 != "" and self.operator != "":
                if (self.operator == "+"):
                    self.operand1 = str(float(self.operand1) + float(self.operand2))
                    self.operand2 = ""
                    self.operator = ""
                    self.model.display = self.operand1

    def button_pressed(self, button_label):
        controller = Controller(self.model)

        if button_label in self.numbers:
            if self.operator == "":
                if self.operand1 == "0":
                    self.operand1 = button_label
                else:
                    self.operand1 += button_label
            else:
                if self.operand2 == "0":
                    self.operand2 = button_label
                else:
                    self.operand2 += button_label
        elif button_label in self.operators:
           self.operator = button_label

        if button_label in self.cancellers:
            print("cancel")
        
        if button_label == "=":
            self.calculate()

        if self.operand2 == "" and self.operator == "":
            self.model.display = self.operand1
        elif self.operand2 == "" and self.operator != "":
            self.model.display = self.operator
        elif self.operand2 != "" and self.operator != "":
            self.model.display = self.operand2

        