# python mini project 1(Student academic info)

print("Students Marks Card".upper()) 
  
print("="*45)


student_name=input("Student name : ")
first_letter=(student_name[0])
print("First letter of the name : ",first_letter)
age=int(input("Age : "))
print("*"*45)


print("Marks Obtained in each Subject".upper())
print("="*45)
kannada=int(input("Kannada : "))
english=int(input("English : "))
sanskrith=int(input("Sanskrith : "))
print("*"*45)

print("Mark".upper())
print("="*45)
total=(kannada+english+sanskrith)
average=total/3
percentage=(total/300)*100
print("Total marks :",total)
print("Average: ", round(average))

print(f"Percentage :{int(percentage)} %")
print("*"*45)

print("very \n good".upper())
print("\t All The best".upper())

print("~"*45)









