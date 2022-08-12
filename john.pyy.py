class animal:
    def noise(self):
        pass
class cat(animal):
    def noise(self):
        print("meoow")
class dog(animal):
    def noise(self):
        print("woof")
class monkey(animal):
    def noise(self):
        print("urrrr")

        
a=cat()
a.noise()                                   #meoow
b=dog() 
b.noise()                                   #woof   
c=monkey()
c.noise()                                   #urrrr




              #method_overriding
           
           
class parent():
    def study(self):
        print("keep studying")
        
class child(parent):
    def study(self):
        print("take  break")
        
c=child()
c.study()


                #operator_overloading
                   
                   

a="hello" ;  b="python"
print(a+b)
c=5 ; d=6
print(c+d)
e=[1,2,3] ; f=[4,5,6]
print(e+f)
print(e[:]+f[:])           #1,2,3,4,5,6