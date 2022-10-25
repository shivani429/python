class NegativeNumberError(Exception):
    pass
class Demo:
    def cube(selfself,a):
        if a>0:
            print(a*a*a)
        else:
            raise NegativeNumberError()
try:
    d=Demo()
    x=int(input("enter any number: "))
    d.cube(x)
except NegativeNumberError:
    print("please pass positive numbers only")
