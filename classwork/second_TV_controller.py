class Controller:
    def __init__(self, TV):
        self.tv = TV

    def turn_off_TV(self):
        self.tv.turn_off()

    def turn_on_TV(self):
        self.tv.turn_on()


class TV:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f'{self.name} turn on')

    def turn_off(self):
        print(f'{self.name} turn off')


tv_1 = TV("sony")
tv_2 = TV("LG")

controllers = [Controller(tv_1), Controller(tv_2)]

for controller in controllers:
    controller.turn_off_TV()


# tv_1 = TV('sony')
# tv_2 = TV('LG')
# tv_3 = TV('samsung')
# contr = Controller(tv_1)
#
# contr.turn_off_TV()