from tkinter import *

def StartUp():
    global val, w, root
    root = Tk()
    root.title('Easy Calc')
    root.geometry('247x330+469+199')
    w = Calculator(root)
    root.mainloop()

class Calculator():
    def __init__(self, root):
        master = Frame(root)
        self.CurrentValue = 0
        self.HolderValue = 0
        self.CurrentFunction = ''
        self.CurrentDisplay = StringVar()
        self.CurrentDisplay.set('0')
        self.DecimalNext = False
        self.DecimalCount = 0
        self.DefineWidgets(master)
        self.PlaceWidgets(master)

    def DefineWidgets(self, master):
        self.lblDisplay = Label(master, anchor=E, relief=SUNKEN, bg="white", height=2, textvariable=self.CurrentDisplay)
        self.btn1 = Button(master, text='1', width=4, height=3)
        self.btn1.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(1))
        self.btn2 = Button(master, text='2', width=4, height=3)
        self.btn2.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(2))
        self.btn3 = Button(master, text='3', width=4, height=3)
        self.btn3.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(3))
        self.btn4 = Button(master, text='4', width=4, height=3)
        self.btn4.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(4))
        self.btn5 = Button(master, text='5', width=4, height=3)
        self.btn5.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(5))
        self.btn6 = Button(master, text='6', width=4, height=3)
        self.btn6.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(6))
        self.btn7 = Button(master, text='7', width=4, height=3)
        self.btn7.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(7))
        self.btn8 = Button(master, text='8', width=4, height=3)
        self.btn8.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(8))
        self.btn9 = Button(master, text='9', width=4, height=3)
        self.btn9.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(9))
        self.btn0 = Button(master, text='0', width=4, height=3)
        self.btn0.bind('<ButtonRelease-1>', lambda e: self.funcNumButton(0))
        self.btnDash = Button(master, text='-', width=4, height=3)
        self.btnDash.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('ABS'))
        self.btnDot = Button(master, text='.', width=4, height=3)
        self.btnDot.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('Dec'))
        self.btnPlus = Button(master, text='+', width=4, height=3)
        self.btnPlus.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('Add'))
        self.btnMinus = Button(master, text='-', width=4, height=3)
        self.btnMinus.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('Subtract'))
        self.btnStar = Button(master, text='*', width=4, height=3)
        self.btnStar.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('Multiply'))
        self.btnDiv = Button(master, text='/', width=4, height=3)
        self.btnDiv.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('Divide'))
        self.btnEqual = Button(master, text='=')
        self.btnEqual.bind('<ButtonRelease-1>', lambda e: self.funcFuncButton('Eq'))
        self.btnClear = Button(master, text='CLEAR')
        self.btnClear.bind('<ButtonRelease-1>', lambda e: self.funcClear())

    def PlaceWidgets(self, master):
        master.grid(column=0, row=0)
        self.lblDisplay.grid(column=0, row=0, columnspan=4, sticky=EW)
        self.btn1.grid(column=0, row=1)
        self.btn2.grid(column=1, row=1)
        self.btn3.grid(column=2, row=1)
        self.btn4.grid(column=0, row=2)
        self.btn5.grid(column=1, row=2)
        self.btn6.grid(column=2, row=2)
        self.btn7.grid(column=0, row=3)
        self.btn8.grid(column=1, row=3)
        self.btn9.grid(column=2, row=3)
        self.btn0.grid(column=1, row=4)
        self.btnDash.grid(column=0, row=4)
        self.btnDot.grid(column=2, row=4)
        self.btnPlus.grid(column=3, row=1)
        self.btnMinus.grid(column=3, row=2)
        self.btnStar.grid(column=3, row=3)
        self.btnDiv.grid(column=3, row=4)
        self.btnEqual.grid(column=0, row=5, columnspan=4, sticky=NSEW)
        self.btnClear.grid(column=0, row=6, columnspan=4, sticky=NSEW)

    def funcNumButton(self, val):
        if self.DecimalNext == True:
            self.DecimalCount += 1
            self.CurrentValue = self.CurrentValue + (val * (10 ** -self.DecimalCount))
        else:
            self.CurrentValue = (self.CurrentValue * 10) + val
        self.DisplayIt()

    def funcClear(self):
        self.CurrentValue = 0
        self.HolderValue = 0
        self.DisplayIt()

    def funcFuncButton(self, function):
        if function == 'Dec':
            self.DecimalNext = True
        else:
            self.DecimalNext = False
            self.DecimalCount = 0
            if function == 'ABS':
                self.CurrentValue *= -1
                self.DisplayIt()
            elif function == 'Add':
                self.HolderValue = self.CurrentValue
                self.CurrentValue = 0
                self.CurrentFunction = 'Add'
            elif function == 'Subtract':
                self.HolderValue = self.CurrentValue
                self.CurrentValue = 0
                self.CurrentFunction = 'Subtract'
            elif function == 'Multiply':
                self.HolderValue = self.CurrentValue
                self.CurrentValue = 0
                self.CurrentFunction = 'Multiply'
            elif function == 'Divide':
                self.HolderValue = self.CurrentValue
                self.CurrentValue = 0
                self.CurrentFunction = 'Divide'
            elif function == 'Eq':
                if self.CurrentFunction == 'Add':
                    self.CurrentValue += self.HolderValue
                elif self.CurrentFunction == 'Subtract':
                    self.CurrentValue = self.HolderValue - self.CurrentValue
                elif self.CurrentFunction == 'Multiply':
                    self.CurrentValue *= self.HolderValue
                elif self.CurrentFunction == 'Divide':
                    self.CurrentValue = self.HolderValue / self.CurrentValue
                self.DisplayIt()
                self.CurrentValue = 0
                self.HolderValue = 0

    def DisplayIt(self):
        print('CurrentValue = {0} - HolderValue = {1}'.format(self.CurrentValue, self.HolderValue))
        self.CurrentDisplay.set(self.CurrentValue)

if __name__ == '__main__':
    StartUp()