def task():
    tasks= [] #empty list
    print("---welcome to the task management system---")

    total_task=int(input("how many tasks do you want to add = "))
    for i in range (0 , total_task):
        task_name= input(f'enter task {i+1}=')
        tasks.append(task_name)
    print(f"the tasks are {tasks}")
     
    while True:
     any_ope=int(input("do you want to perfrom any operations? "))
     if any_ope== 1:
        operation = int(input("enter\n 1-add\n 2-update\n 3-delete\n 4-view\n 5-stop \n= "))
        if operation ==1:
            add= input("enter the task you want to add: ")
            tasks.append(add)
            print(f"you have succesfully added the {add}")
            
    

        elif operation ==2 :
            already = input("enter the task you want to update : ")
            if already in tasks:
                updated = input("enter the new task: ")
                ind= tasks.index(already)
                tasks[ind]=updated
        elif operation ==3:
            delete=input("enter the task to delete: ")
            if delete in tasks:
                tasks.remove(delete)
            print("the tasks after deletion are: ",tasks)
        elif operation ==4 :
            print("the tasks are: ",tasks)
        elif operation==5:
            print("Closing the program")
            break
        else:
            print("Invalid operation")
     else:
      break
            
task()


