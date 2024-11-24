#To-Do List project

#Variables
Tasks = []
Task = []

#Functions
def createTask():
    newTask = input("Ingrese su nueva actividad pendiente!: ")
    Task.append(newTask) #add newTask in a new task list

    state = input("\nSe recomiendan el uso de 'Pendiente' y 'Completada'\nEstado de su tarea?: ")
    Task.append(state) #add state of newTask
    
    Tasks.append(Task) #add new task list with its state in Tasks (it contain all tasks)

def showTasks():
    for t in Tasks:
        for s in t:
            print("Tarea: ",s)
            print("Estado: ", s)  #nota Mejorar diseno para imprimir estado de la terea.
#def deleteTask():

#MAIN
createTask()
showTasks()