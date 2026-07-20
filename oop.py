#oop in python
#to map with real world scenarios,we use objects in code

#class is blueprint for creating objects
#creating class
class Students:
    name="Janvi Yadav"

#creating object
s1=Students()
print(s1.name)

s2=Students()
print(s2.name)

#constructor
class Cars:
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        print("New Cars in the market..")

c1 = Cars("BMW","Black")
print(c1.brand, c1.color)

c2 = Cars("Mercedes","white")
print(c2.brand, c2.color)

#class attribute and object attribute
#object attribute has higher preference than class object
class Students:
    College_name="Ajeenkya DY Patil" #class sttribute , same for every object
    name="none" #use when no name data is given 
    def __init__(self,name,marks):
        self.name=name #object attribute
        self.marks=marks

s1=Students("Janvi",9.33)
s2=Students("Tanushri",9.78)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s1.College_name) 

#methods= functions that belongs to objects
class Students:
    college_name="adypsoe"

    #constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #methods
    def welcome(self):
        print("welcome,",self.name)

    def get_marks(self): 
        return self.marks

s1=Students("Janvi",9.33)
s1.welcome()
print(s1.get_marks())

#qs1
class Employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_avg(self):
        sum=0
        for val in self.salary:
            sum+=val
        print(e1.name,"Avg salary is,",sum/3)

e1=Employees("Tanushri",[40000,50000,55000])
print(e1.get_avg())

#static methods = methods that dont use self parameter , works at class level
class Students:
    college_name="adypsoe"

    #constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    #static methods
    @staticmethod  #decorator
    def welcome():
        print("welcome")

    def get_marks(self): 
        return self.marks

s1=Students("Janvi",9.33)
s1.welcome()
