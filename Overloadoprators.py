class A():
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a < other.a:
            return "Ob1 is less than Ob2."
        else:
            return "Ob2 is less than Ob1."
    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "They are not equal."
Ob1 = A(6)
Ob2 = A(3)
print("The passed values are : ",Ob1.a, Ob2.a)
print(Ob1 < Ob2)
Ob3 = A(5)
Ob4 = A(5)     
print("The passed values are : ",Ob3.a, Ob4.a)   
print(Ob3 == Ob4)