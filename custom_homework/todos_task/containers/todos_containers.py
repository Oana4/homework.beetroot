
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

    @classmethod
    def show_all_tasks(cls):
        for todo in cls.list_of_todos:
            print(todo)

    @classmethod
    def show_missed_tasks(cls):
        for todo in cls.list_of_todos:
            if todo.past_due_date():
                print(todo)

    @classmethod
    def find_tasks_for_today(cls):
        for todo in cls.list_of_todos:
            if todo.todays_date():
                print(todo)


