#Weekend Planner

day=input("Enter the day of today: ").strip().lower()
print(f"\nWhat did you say, today is {day}!!")

if day in ['saturday', 'sunday']:
    print("yeah! Today is a fun day..")
else:
    print("Work! Work! Work!...")

plans=[]

if day in ['saturday', 'sunday']:
    print(f"\nwhat's on your mood today? ")
    print("1.Chill with friends..")
    print("2.Will sleep the whole day")
    print("3.Enhance my python skills")
    print("Type 'q' or 'done' to finsh planning.\n")
    while True:
         option=input("please choose your plan from options 1/2/3 or type 'q'/'done' to quit: ").strip().lower()
         if option not in ("1","2","3"):
                print("No plans, just go with the flow..")
                plans.append("No plans, just go with the flow..")
                break
         elif option=="1":
                plans.append("Chill with friends..")
                print("Noted- Chill with friends")
         elif option=="2":
                plans.append("Will sleep the whole day")
                print("Noted- Will sleep the whole day")
         elif option=="3":
                plans.append("Enhance my python skills")
                print("Noted- Enhance my python skills")   
         elif option in ["q","done"]:
                print("\nWeekend's planning Completed!")
                break
         else:
                print("No plans, just go with the flow..")
                plans.append("No plans, just go with the flow..")
else:
    print(f"\nWhat is the plan?\nCan't Plan! Need to go for work..")
    plans.append("Grind in Office!!")

print("\n Summary of today's plans: ")
for p in plans:
    print("-",p)
