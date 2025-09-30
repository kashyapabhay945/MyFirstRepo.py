skills=["Python","Machine Learning","Cloud Computing"]
data=[]
top_emp=""
top_rating=0
def ra(r):
    if r>8:
        return "WOW"
    elif r>5:
        return "Good"
    elif r>3:
        return "Need training"
    else:
        return "Not expected"

while True:
    print("Please choose from the below options:\n1. Add Employee\n2. Show All Employees\n3. Search by Name\n4. Save to file(JSON)\n5. Load from file(JSON)\n6. Exit")
    option=input("1/2/3/4/5/6 which one? ")
    if option=="1":
        confirmation=input("You have selected option 1.Add Employee, confirm Y/N: ")
        if confirmation.upper()!="N":
            total_emp=int(input("Numbers of employees you want to add: "))
            for i in range(total_emp):
                name=input(f"Enter the name of employee{i+1}: ").strip().title()
                rating=[]
                for skill in skills:
                    r=int(input(f"Please rate {name}'s knowledge of {skill} on the scale of 0to10: "))
                    rating.append(r)
                added={"name":name,"rating":rating}
                data.append(added)
            Print=input("print data Y/N: ")
            if Print.upper()=="Y":
              print(f"\ndata\n")
        continue
    elif option=="2":
        confirmation=input("You have selected option 2.Show All Employees, confirm Y/N: ")
        if confirmation.upper()!="N":
            for employee in data:
                get_name=employee["name"]
                get_rating=employee["rating"]
                total=sum(get_rating)
                average=total/len(get_rating)
                print(f"\n {get_name} rating as per Skills:")
                for skill,r in zip(skills,get_rating):
                    R=ra(r)
                    print(f"{skill}:{r}->{R}")
                    
                print(f"\nTotal of {get_name} is {total} with average:{average:.2f}\n")

                if total>top_rating:
                    top_emp=get_name
                    top_rating=total
            print(f"\nTop Employee is {top_emp} with the rating {top_rating}")
        continue
    elif option=="3":
        confirmation=input("You have selected option 3.Search by Name, confirm Y/N: ")
        if confirmation.upper()!="N":
            search=input("Enter the name you want to search: ").strip()
            found=False
            print(f"\n {search} rating as per Skills:")
            for employee in data:
                if search.lower()==employee["name"].lower():
                    found=True
                    for skill,r in zip(skills,rating):
                        R=ra(r)
                        print(f"\n{skill}:{r}->{R}")
        continue
    elif option=="4":
        confirmation=input("You have selected option 4.Save to file(JSON), confirm Y/N: ")
        if confirmation.upper()!="N":
            import json
            file=open("employee.json","w")
            json.dump(data,file)
            file.close()
        continue
    elif option=="5":
        confirmation=input("You have selected option 5.Load from file(JSON), confirm Y/N: ")
        if confirmation.upper()!="N":
            import json
            
            file=open("employee.json","r")
            data=json.load(file)
            print(f"\ndata")
            file.close()
        continue
    elif option=="6":
        confirmation=input("You have selected option 6.Exit, confirm Y/N: ")
        if confirmation.upper()=="Y":
            print("Thanks for Visiting, Exiting the Program")
        break
    else:
        print("Invalid choice!!,Try again:)")
        continue