# Question 1
class Loan:
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000, borrower=""):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (self.__numberOfYears * 12))
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment


loan1 = Loan()
loan1.setAnnualInterestRate(90)
loan1.setNumberOfYears(1)
print(loan1.getTotalPayment())

# Question 2
class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        bmi = self.__weight / (self.__height ** 2)
        return bmi

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        else:
            return "Overweight"

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height

bmi1 = BMI("Ali", 25, 70, 1.75)
print(bmi1.getBMI())
print(bmi1.getStatus())

# Question 3
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

# Question 4
class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            print("Denominator cannot be zero.")
        if denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            self.numerator = numerator
            self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            print("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return RationalNumber(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
r1 = RationalNumber(1, 2)
r2 = RationalNumber(3, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)

# Question 5
class Polynomial:
    def __init__(self, terms=None):
        self.terms = {}
        if terms:
            for coef, exp in terms:
                self.set_term(coef, exp)

    def __del__(self):
        self.terms.clear()

    def set_term(self, coef, exp):
        if coef == 0:
            self.terms.pop(exp, None)
        else:
            self.terms[exp] = self.terms.get(exp, 0) + coef

    def get_term(self, exp):
        return self.terms.get(exp, 0)
    
    def copy(self):
        new_poly = Polynomial()
        new_poly.terms = self.terms.copy()
        return new_poly
    
    def __add__(self, other):
        result = self.copy()
        for exp, coef in other.terms.items():
            result.set_term(coef, exp)
        return result

    def __sub__(self, other):
        result = self.copy()
        for exp, coef in other.terms.items():
            result.set_term(-coef, exp)
        return result


    def __mul__(self, other):
        result = Polynomial()
        for exp1, coef1 in self.terms.items():
            for exp2, coef2 in other.terms.items():
                new_coef = coef1 * coef2
                new_exp = exp1 + exp2
                result.set_term(new_coef, new_exp)
        return result


    def __iadd__(self, other):
        for exp, coef in other.terms.items():
            self.set_term(coef, exp)
        return self

    def __isub__(self, other):
        for exp, coef in other.terms.items():
            self.set_term(-coef, exp)
        return self

    def __imul__(self, other):
        result = self * other 
        self.terms = result.terms
        return self

    def __str__(self):
        if not self.terms:
            return "0"

        parts = []
        for exp in sorted(self.terms.keys(), reverse=True):
            coef = self.terms[exp]
            parts.append(f"{coef}x^{exp}")

        return " + ".join(parts).replace("+ -", "- ")

if __name__ == "__main__":
    p1 = Polynomial([(2, 4), (3, 2)])  # 2x^4 + 3x^2
    p2 = Polynomial([(1, 4), (-1, 0)]) # 1x^4 - 1x^0
    
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    
    print(f"p1 + p2: {p1 + p2}")
    print(f"p1 - p2: {p1 - p2}")
    print(f"p1 * p2: {p1 * p2}")
    
    p1 += p2
    print(f"p1 after += p2: {p1}")