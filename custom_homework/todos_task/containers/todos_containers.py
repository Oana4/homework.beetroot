
class ListOfTodos:

    list_of_todos = []

    @classmethod
    def add_todo(cls, todo):
        cls.list_of_todos.append(todo)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list_of_todos):
            temp_index = self.index
            self.index += 1
            return self.list_of_todos[temp_index]
        else:
            raise StopIteration()

    def show_all_tasks(self):
        for todo in self.list_of_todos:
            print(todo)

    def show_missed_tasks(self):
        for todo in self.list_of_todos:
            if todo.past_due_date():
                print(todo)

    def find_tasks_for_today(self):
        for todo in self.list_of_todos:
            if todo.todays_date():
                print(todo)


