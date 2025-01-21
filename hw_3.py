class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f'CPU: {self.cpu}GHz, Memory: {self.memory}Gb'

    def __lt__(self, other):
        return self.memory < other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        pass

    def call(self, sim_card_operator, call_to_number):
        print(f'A call is coming to the number: {call_to_number}, from SIM card: {sim_card_operator} - {self.__sim_cards_list[sim_card_operator - 1]}')

    def __str__(self):
        return f'Phone with {self.sim_cards_list} SIM card'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Phone.__init__(self, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        print(f'The route from your location to the location: {location} has been successfully plotted')

    def __str__(self):
        return f'CPU: {self.cpu}GHz, Memory: {self.memory}Gb, SIM card: {self.sim_cards_list}'


computer1 = Computer(4, 8)
phone1 = Phone(['Beeline', 'O!', 'Mega'])
smartphone1 = SmartPhone(2, 8, ['Beeline', 'O!', 'Mega'])
smartphone2 = SmartPhone(4, 8, ['Beeline', 'O!', 'Mega'])

print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

print(f'The result of computer calculations: {computer1.make_computations()}')

phone1.call(1, '+996 777 99 88 11')
phone1.call(2, '+996 709 80 11 21')
phone1.call(3, '+996 505 60 32 22')

smartphone1.use_gps('TSUM')
smartphone2.use_gps('Asanbay center')

print(f'Memory of computer1 is equal to memory of smartphone1: {computer1 == smartphone1}')
print(f'Memory of computer1 is not equal to memory of smartphone1: {computer1 == smartphone1}')
print(f'Memory of computer1 is smaller than memory of smartphone1: {computer1 < smartphone1}')
print(f'Memory of computer1 is smaller or equal to memory of smartphone1: {computer1 < smartphone1}')
print(f'Memory of computer1 is bigger then memory of smartphone1: {computer1 <= smartphone1}')
print(f'Memory of computer1 is bigger of equal to memory of smartphone1: {computer1 <= smartphone1}')

