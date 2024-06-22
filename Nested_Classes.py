#concept of Nested Class
class GovtSchool(object): #Outer Class
    def __init__(self,n,pn):
        self.schoolname=n
        self.principalname=pn
        self.c=self.TenBlue("Asif Sahb",56,"Amir") #Object of Inner Class
    def show(self):
        print("School Name",self.schoolname)
        print("School Head Name",self.principalname)
    class TenBlue(object): #Inner Class
        def __init__(self,n,t,cr):
            self.inchargename=n
            self.strength=t
            self.crname=cr
        def display(self):
            print("Incharge name",self.inchargename)
            print("Total Strength of Class",self.strength)
            print("Class CR name",self.crname)

a=GovtSchool("Govt. High School Usman Wala","Malik Asghar ali") #Object of Outer Class
a.show() #Run instance method of outer Class
b=GovtSchool("Govt. High School Usman Wala","Malik Asghar ali").TenBlue("Hameed Sahb",48,"Gulzar") #Object of Inner class
b.display() #Run instance method of inner Class 
print()
a.c.display() #Run instance method of outer Class
print()
d=a.c #Create Object of Inner class with the Help of Outer Class Object 
d.display() #Run instance method of outer Class
