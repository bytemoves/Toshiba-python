class fruits:
    def __init__(self, type, price, color):

        self.type = type
        self.price = price
        self.color = color
    def show(self):
        print(f"i like eating{self.type},and it cost{self.price},color{self.color}")
obj = fruits("banana",12,"yellow")
obj2 = fruits("apples",40,"blue")
obj.show()
obj2.show()
