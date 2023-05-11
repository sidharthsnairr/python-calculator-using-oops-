class calculator():
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("sum", self.num1+self.num2)
    def sub(self):
        print("sub",self.num1 - self.num2)
    def mul(self):
        print("mul",self.num1*self.num2)
    def div(self):
        print("div",self.num1/self.num2)
num1=int(input("enter the first number::"  ))
num2=int(input("enter the second number::"  ))

Arithmetic=calculator(num1 , num2)
print("which operation should be done first")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
select=input("enter the correct option: [1/2/3/4]::" )
if select=="1":
    Arithmetic.add()
elif select=="2":
    Arithmetic.sub()
elif select=="3":
    Arithmetic.mul()
elif select=="4":
    Arithmetic.div()
else:
    print("invalid option")
    exit()
