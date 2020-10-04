def health(num): #function to determine time suitable for that particular health problem
    pass

def gender(gen): #function to determine time suitable for that particular gender
    pass

def age_group(age): #function to determine time suitable for that particular age_group
    pass

def BMI(height,weight): #function to determine BMI of the astronaut
    bmi = weight/(height**2)
    print("Your BMI(Body Mass Index is )",bmi)

DATA = []
num = 2

for i in range(0,num):

    name = input("Please enter your name: ")
    print("Hello ",name,"! I need you to answer certain questions before I could plan out a time-table.")

    print("\nPress 1 for Male\nPress 2 for Female")
    gen = int(input())
    gender(gen)

    print("\nPress 1 for 2-16 age group\nPress 2 for 17-30 age group\nPress 3 for 31-60 age group\nPress 4 for 61 and above age group")
    age = int(input())
    age_group(age)

    print("\nPress 1 if you have any health problems, else Press 2")
    heal = int(input())
    health(heal)

    print("\nEnter your height")
    height = int(input())

    print("\nEnter your weight")
    weight = int(input())

    BMI(height,weight)

    ASTRO_DATA = [name,gen,age,heal,BMI]
    DATA.append(L)

print(B)
