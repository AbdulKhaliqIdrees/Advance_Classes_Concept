#Passing Members of one Class to another Class 
#Correct use of Static Method
#Example of Static Method
class School(object): #First Class
    def __init__(self,n,c):
        self.teachername=n
        self.totalstudents="100"
        self.totaldesks="50"
        self.totalChairs=c
    def show(self):
        print("Head of  School",self.teachername)
        print("Total Strength of School",self.totalstudents)
        print("Total desks in School",self.totaldesks)
        print("Total Chairs in School",self.totalChairs)
class TenGreen():  #Second Class
    @staticmethod
    def display(v): #Static method
        print("Head of  TenGreen",v.teachername)
        print("Total Strength of TenGreen",v.totalstudents)
        print("Total desks in TenGreen",v.totaldesks)
        print("Total Chairs in TenGreen",v.totalChairs)
        print()
        v.show() #Run instance method of First Class in Static method of Second Class


a=School("Abdul Khaliq",1) #Object of First Class
TenGreen.display(a) #Run static method with the name of Second Class
print()
b=TenGreen() #Object of Second Class
b.display(a) #Run static method with the Object of Second Class

