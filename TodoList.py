#To-Do List project
from operator import index

#Variables
Task = []
Tasks =[]

#Functions
def createTask():
    follow = 1

    while follow == 1:
        newTask = input("Enter your new Task!: ")
        Task.append(newTask) #add newTask in a new task list

        state = input("\nWe recommend use 'Pendient' or 'completed' word.\nEstate of your task?: ")
        Task.append(state) #add state of newTask
        Tasks.append(Task[:])  # add new task list (no reference, its COPY of Task) with its state in Tasks (it contain all tasks)

        Task.clear() #clear task list for add new task list in Tasks (it contain all tasks)

        follow = int(input("Do you want continue?: \nPress [1] for YES\nPress [0] for NO: "))
        if follow != 1:
            break

def showTasks():
    y = 1
    for t in Tasks:
        print("\n--- Task N",y,"---")
        print("To do: ",t[0])
        print("Estate: ",t[1])
        y+=1

def deleteTask():
    print("\nWe recommending look yours task first before delete something")
    showTasks()
    selector = int(input("--- Which one you wan delete? ---\nEnter number of task you wan delete: "))
    Tasks.pop(index(selector-1))

#MAIN
createTask()
showTasks()
deleteTask()
showTasks()