from PIL.ImImagePlugin import number

print("Do you want to check your grade & grade point according to your mark ?")

mark = float(input("Enter mark:" ))

if mark >= 80 and mark <= 100:
    print("Grade is: A+")
    print("Grade point is: 5 out of 5")
elif mark >= 70 and mark < 80:
    print("Grade is: A")
    print("Grade point is: 4 out of 5")
elif mark >= 60 and mark < 70:
    print("Grade is: A-")
    print("Grade point is: 3.5 out of 5")
elif mark >= 50 and mark < 60:
    print("Grade is: B")
    print("Grade point is: 3 out of 5")
elif mark >= 40 and mark < 50:
    print("Grade is: C")
    print("Grade point is: 2 out of 5")
elif mark >= 33 and mark < 40:
    print("Grade is: D")
    print("Grade point is: 1 out of 5")
else:
    print("Fail")



