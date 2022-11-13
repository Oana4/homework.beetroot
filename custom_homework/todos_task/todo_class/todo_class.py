from datetime import datetime, timedelta


class ToDo:

    possible_status = ['created', 'in progress', 'finished']

    def __init__(self, status, description, due_date: str):
        self._status = status
        self._description = description
        self._due_date = datetime.strptime(due_date, '%Y/%m/%d %H:%M')

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status in self.possible_status:
            self._status = new_status
            print(f"Status updated to {new_status}!")
        else:
            print("Choose a valid status!")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description
        print(f"Description updated to {new_description}!")

    @description.deleter
    def description(self):
        self._description = ''

    # def a_day_before(self):
    #     return self.due_date - timedelta(days=1)

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, new_due_date):
        self._due_date = datetime.strptime(new_due_date, '%Y/%m/%d %H:%M')
        print(f"due_date updated to {new_due_date}!")

    def past_due_date(self):
        if self.status != 'finished' and datetime.now() > self.due_date:
            return True
        return False

    def todays_date(self):
        if self.status != 'finished' and self.due_date.date() == datetime.today().date():
            return True
        return False

    def __str__(self):
        return f"Status: {self.status}\n" \
               f"Description: {self.description}\n" \
               f"Due date: {self.due_date.strftime('%Y/%m/%d %H:%M')}."




    
    


