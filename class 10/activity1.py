total_chores = 4 
completed_count = 0
chore_num = 1

print(f"you have {total_chores} chores")

while completed_count<total_chores:
    if chore_num==1: chore="Do your laundry"
    elif chore_num==2: chore="Feed the pet"
    elif chore_num==3: chore="Do the dishes"
    elif chore_num==4: chore="Clean your room"

    answer=input(f"Have you done the:  {chore} (yes/no)").strip().lower()
    if answer=="yes":
        print("Good, keep up the good work")
        completed_count+=1
        chore_num+=1
    else:
        print("Please hurry up and complete your chores")
    print(f"Number of chores left: {total_chores-completed_count}")
print("All the chores are completed, well done")

test_value=0
safety_count=0
while test_value<=0:
    print("Hello world")
    if safety_count==3:
        print("Stop.")
        break
    safety_count+=1

print("Tasks completed:", completed_count)
print("Total tasks", total_chores)
print("Remaining chores:", total_chores-completed_count)