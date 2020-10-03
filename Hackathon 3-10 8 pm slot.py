class sleep:
    def __init__(self,health,gender,age_group,height,weight):
        self.health = health
        self.gender = gender
        self.age = age
        self.age_group = age_group
        self.height = height
        self.weight = weight

    
    def BMI(self):
        pass
        
num = int(input("Enter number of astronauts = "))
L = []

for i in range(0,num):

    name = input("Please enter your name: ")
    print("Hello ",name,"! I need you to answer certain questions before I could plan out a time-table.")

    print("\nPress 1 for Male\nPress 2 for Female")
    gen = int(input())

    print("\nPress 1 for 2-16 age group\nPress 2 for 17-30 age group\nPress 3 for 31-60 age group\nPress 4 for 61 and above age group")
    age = int(input())

    print("\nPress 1 if you have any health problems, else Press 2")
    heal = int(input())

    print("Enter Height = ")
    height = int(input())

    print("Enter Weight = ")
    weight = int(input())

    L.append(sleep(heal,gen,age,height,weight))
    
print(type(L))
print(L)







    
