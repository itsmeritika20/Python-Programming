#operations on complex number
class Complex:
    def getdata(self):
        self.r = int(input("Enter real number:"))
        self.i = int(input("Enter imaginary number:"))
    def mul(self, c2):
        self.r = self.r * c2.r
        self.i = self.i * c2.i
    def display(self):
        print("\nMultiplication:\n", str(self.r), "*" ,str(self.i),"i")
c1 = Complex()
c2 = Complex()

print("\nIn first num:")
c1.getdata()
print("\nIn second num:")
c2.getdata()

c1.mul(c2)
c1.display()