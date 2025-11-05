#project : discount eligibility checker based on age (Mst.Marjeya)
age= int(input("enter age: "))
member = input("Are you a member? (yes/no):")
date = input("enter date (lower case):")
discount=0

if age<18 or age>65:
    discount+= 10
if member== "yes":
    discount +=10
    if member== "no":
        discount = 0
    if date== "friday" or date=="saturday":
         discount +=5
    print("your discount:" , discount )