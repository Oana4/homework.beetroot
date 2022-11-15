import custom_homework.todos_task.containers.todos_containers as container
import custom_homework.todos_task.todo_class.todo_class as todo


my_container = container.ListOfTodos()

task_1 = todo.ToDo('created', 'go shopping', '2022/11/15 20:00')
my_container.add_todo(task_1)
print("Current status ", task_1.status)
task_1.status = 'mejkw'
task_1.status = 'in progress'
print(task_1)
print("\n")


task_2 = todo.ToDo('created', 'finish book', '2022/11/12 15:00')
my_container.add_todo(task_2)
print(task_2)
print("\n")
# print all tasks
print("All tasks: ")
print(container.ListOfTodos.show_all_tasks())
print("\n")
# print un-done tasks
print("Missed tasks: ")
print(container.ListOfTodos.show_missed_tasks())
print("\n")
# print today's tasks
print("Today's tasks: ")
print(container.ListOfTodos.find_tasks_for_today())




