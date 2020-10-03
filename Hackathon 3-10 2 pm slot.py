def health(num):
    pass

def gender(gen):
    pass

def age_group(age):
    pass


name = input("Please enter your name: ")
print("Hello ",name,"! I need you to answer certain questions before I could plan out a time-table.")

print("\n\nPress 1 for Male\nPress 2 for Female")
gen = int(input())
gender(gen)

print("\n\nPress 1 for 2-16 age group\nPress 2 for 17-30 age group\nPress 3 for 31-60 age group\nPress 4 for 61 and above age group")
age = int(input())
age_group(age)

print("\n\nPress 1 if you have any health problems, else Press 2")
heal = int(input())
health(heal)


