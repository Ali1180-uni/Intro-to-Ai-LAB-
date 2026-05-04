from tkinter import *


class MenuDemo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Loan Calculator")

        self.frame1 = Frame(self.window, padx=10, pady=10)
        self.frame1.grid(row=0, column=0, sticky=W)

        Label(self.frame1, text="Annual Interest Rate").grid(row=0, column=0, sticky=W, pady=2)
        self.v1 = StringVar()
        Entry(self.frame1, width=20, textvariable=self.v1, justify=RIGHT).grid(row=0, column=1, pady=2)

        Label(self.frame1, text="Number of Years").grid(row=1, column=0, sticky=W, pady=2)
        self.v2 = StringVar()
        Entry(self.frame1, width=20, textvariable=self.v2, justify=RIGHT).grid(row=1, column=1, pady=2)

        Label(self.frame1, text="Loan Amount").grid(row=2, column=0, sticky=W, pady=2)
        self.v3 = StringVar()
        Entry(self.frame1, width=20, textvariable=self.v3, justify=RIGHT).grid(row=2, column=1, pady=2)

        Label(self.frame1, text="Monthly Payment").grid(row=3, column=0, sticky=W, pady=2)
        self.v4 = StringVar()
        Entry(self.frame1, width=20, textvariable=self.v4, justify=RIGHT).grid(row=3, column=1, pady=2)

        Label(self.frame1, text="Total Payment").grid(row=4, column=0, sticky=W, pady=2)
        self.v5 = StringVar()
        Entry(self.frame1, width=20, textvariable=self.v5, justify=RIGHT).grid(row=4, column=1, pady=2)

        self.frame2 = Frame(self.window, padx=10, pady=10)
        self.frame2.grid(row=1, column=0, sticky=E)
        Button(self.frame2, text="Compute Payment", command=self.add).grid(row=0, column=0, sticky=E)

        self.window.mainloop()

    def calculatePayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)))
        totalPayment = monthlyPayment * numberOfYears * 12
        return monthlyPayment, totalPayment

    def add(self):
        monthlyPayment, totalPayment = self.calculatePayment(float(self.v3.get()), float(self.v1.get()) / 1200, int(self.v2.get()))
        self.v4.set(format(monthlyPayment, "10.2f"))
        self.v5.set(format(totalPayment, "10.2f"))

MenuDemo()
