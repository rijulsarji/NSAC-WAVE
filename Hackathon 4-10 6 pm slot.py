import random

def gender(gen): #function to determine time suitable for that particular gender
    sleep_gen = 0

    if gen == 1:
        sleep_gen = -2
    elif gen == 2:
        sleep_gen = -1

    return sleep_gen
        
def age_group(age): #function to determine time suitable for that particular age_group
    sleep_age = 0

    if age == 1:
        sleep_age = 12
    elif age == 2:
        sleep_age = 10
    elif age == 3:
        sleep_age = 8
    elif age == 4:
        sleep_age = 9

    return sleep_age
        

def BMI(height,weight): #function to determine BMI of the astronaut

    sleep_bmi = 0
    bmi = (weight/(height**2))*10000

    if bmi >=30:
        sleep_bmi = -2
    elif bmi >=25 and bmi <30:
        sleep_bmi = -1
    else:
        sleep_bmi = 0
   
    print("Your BMI(Body Mass Index is)",bmi)
    return sleep_bmi

DATA = []
num = int(input("Please enter number of astronauts = "))

for i in range(0,num):

    print("ASTRONAUT ",i+1)
    print()
    name = input("Please enter your name: ")
    print("Hello ",name,"! I need you to answer certain questions before I could plan out a time-table.")

    print("\nPress 1 for Male\nPress 2 for Female")
    gen = int(input())
    SG = gender(gen)

    print("\nPress 1 for 0-16 age group\nPress 2 for 17-30 age group\nPress 3 for 31-50 age group\nPress 4 for 51 and above age group")
    age = int(input())
    SA = age_group(age)

    print("\nEnter your height")
    height = int(input())

    print("\nEnter your weight")
    weight = int(input())

    SB = BMI(height,weight)

    blah = 0    
    tot_sleep = SG+SA+SB
    time = random.randint(0,24)
    end_time = time+tot_sleep
    gap = ''


    if end_time > 24:
        blah = end_time - 24
        end_time = blah
        if end_time<10:
            gap = '0'
        
    
    print()
    print("you require",tot_sleep,"hours of sleep.")
    print()

    if time<10:
        print("Your sleep schedule is from ","%02d" % time ,'00'," hrs to ",gap,end_time*100," hrs",sep = '')
    else:
        print("Your sleep schedule is from ",time*100," hrs to ",gap, end_time*100," hrs",sep = '')
    ASTRO_DATA = [name,gen,age]
    DATA.append(ASTRO_DATA)
    print()

#print(DATA)
