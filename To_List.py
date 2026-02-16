def task():
    tasks=[]
    print("----Wlecome to the task management app----")

    total_task=int(input("Enter how many task you want to add"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are \n {tasks}")
    while(True):
        operation=int(input(r"Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Stop"))

        if operation==1:
            add=input("Enter task you want ot add = ")
            tasks.append(add)
            print(f"Task {add} has been added..")
        elif operation==2:
            updated_val=input("Enter the task name you want ot update")
            if updated_val in tasks:
                up=input("Enter new task = ")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"Updated task {up}")
        elif operation==3:
            delete_val=input("Which task you want ot delete")
            if(delete_val in tasks):
                ind=tasks.index(delete_val)
                del tasks[ind]
                print(f"Deleted value = {delete_val}")
        
        elif operation ==4:
            print(f"Total tasks = {tasks}")
        elif operation==5:
            print("Closing the list.....")
            break 
        else:
            print("Invalid input.....")
        


task()