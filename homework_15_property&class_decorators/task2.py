# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, new_worker):
        if not isinstance(new_worker, Worker):
            raise TypeError("object is not a Worker class instance")
        self._workers.append(new_worker)

    def __repr__(self):
        return f"id: {self.id}\nname: {self.name}\ncompany: {self.company} \n"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss_name):
        if not isinstance(boss_name, Boss):
            raise TypeError("object is not a Boss class instance")
        self._boss = boss_name

    def __repr__(self):
        return f"id: {self.id}\nname: {self.name}\ncompany: {self.company}\nboss: {self._boss.name} \n"


boss_1 = Boss(1, 'Johnson', 'P&G')
boss_2 = Boss(2, 'Anderson', 'Great Cuisine')
worker_1 = Worker(231, 'Johnny', 'Great Cuisine', boss_1)
worker_1.boss = boss_2
worker_2 = Worker(428, 'Ada', 'P&G', boss_1)
boss_1.workers = worker_2
print(boss_1)
print(boss_1.workers)
print("\n")
print(worker_1)





