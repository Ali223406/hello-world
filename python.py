First_Name=input()
Last_Name=input()
print("Bonjour" + First_Name + " " + Last_Name)
print("coco")
print("What is your age")
Age=int(input())
if Age<0 :
 print("Error")
elif Age>110:
 print("Error")
elif Age<18:
 print("What is the name of your legal representator")
 Name=(input())
 print("What is the surname of your legal representator")
 surname=(input())
 print(Name +" "+ surname)
else:
 print("Major")

