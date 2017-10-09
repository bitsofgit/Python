
class SomeClass:
    someStaticVar = "Static Var"

    def __init__(self, someClassVar):   # constructor
        self.someClassVar = someClassVar
        print("In SomeClass constructor : " + self.someClassVar)

    def __str__(self):
        return "SomeClass " + self.someClassVar

    def SomeFunction(self, j, k):
        return j + k

class InheritedClass(SomeClass):
    def SomeFunction(self, j, k):  # override SomeFunction
        orignal_val = super().SomeFunction(j, k)  # way to call base class method
        return orignal_val * 2
