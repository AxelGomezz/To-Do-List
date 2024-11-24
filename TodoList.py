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

        state = input("\n|-- We recommend use 'Pendient' or 'completed' word. --|\nEstate of your task?: ")
        Task.append(state) #add state of newTask
        Tasks.append(Task[:])  # add new task list (no reference, its COPY of Task) with its state in Tasks (it contain all tasks)

        Task.clear() #clear task list for add new task list in Tasks (it contain all tasks)

        follow = int(input("\nDo you want continue?: \nPress [1] for YES\nPress [0] for NO: "))
        if follow != 1:
            break

def showTasks():
    y = 1
    for t in Tasks:
        print("\n    Task N",y,"   ")
        print("To do: ",t[0])
        print("Estate: ",t[1])
        y+=1

def deleteTask():
    print("\n|-- We recommending look yours task first before delete something --|")
    showTasks()
    selector = int(input("\n|-- Which one you wan delete? --|\nEnter number of task you wan delete: "))
    Tasks.pop(index(selector-1))

def changeStatus():
    print("\n|-- We recommending look yours task first before delete something --|")
    showTasks()
    selector = int(input("\n|-- Which task you wan change its Status? --|\nEnter number of task you wan change status: "))
    Tasks[selector-1][1] = input("What is the new status of this stask: ")

#MAIN
createTask()
deleteTask()
changeStatus()
showTasks()