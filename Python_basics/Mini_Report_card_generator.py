total_students=int(input("Total number of students: "))
data=[]

for i in range(total_students):
    name=input(f"Enter the name of student{i+1}: ").strip().title()
    mark=int(input(f"Enter the marks of '{name}' in python test: "))
    
    data.append((name,mark))

total=0
topper_name=""
topper_marks=0
topper_grade=""

for student in data:
    name=student[0]
    mark=student[1]
   
    total=total+mark

    
    if mark>=75:
        grade="A+"
    elif mark>=35:
        grade="B+"
    else:
        grade="F"

    if mark>topper_marks:
        topper_name=name
        topper_marks=mark
        topper_grade=grade
    print("\n-------------------------Student's Report--------------------------------------")
    print(f"Name:{name}")
    print(f"Marks: {mark}")
    print(f"Grade: {grade}")
    print("---------------------------------------------------------------\n")

average=total/total_students
print("\n--------------------Class summary of today's test---------------------------")
print(f"Average marks: {average:.2f}")
print(f"Topper is '{topper_name}', secured highest marks i.e., {topper_marks} out of 100 with '{topper_grade}' performance in today's python test.\n......KEEP IT UP!!....")
print("-----------------------------------------------------------END OF REPORT-------------------------------------------------------------")