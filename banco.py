from random import choice
from os import system


class Persona:    
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        

class Cliente(Persona):
    def __init__(self, name, last_name, number_count, income):
        super().__init__(name, last_name)
        self.number_count = number_count
        self.income = income
        
    def __str__(self) -> str:
        return f'''Nombre: {self.name}
Apellido: {self.last_name}
No. Cliente: {self.number_count}
Saldo disponible: {self.income}
'''

    def deposit(self):
        print(f'Saldo disponible: {self.income}')
        amount_deposit = int(input('¿Cuanto deseas depositar?'))
        print(f'{self.income} + {amount_deposit}')
        self.income += amount_deposit
        print(f'Saldo disponible {self.income}')
        
    
    def withdraw(self):
        print(f'Saldo disponible: {self.income}')
        amount_withdraw = int(input('¿Cuanto deseas retirar?'))
        if self.income < amount_withdraw:
            print('No tienes saldo suficiente para realizar esta transaccion')
        else:
            print(f'{self.income} - {amount_withdraw}')
            self.income -= amount_withdraw
            print(f'Saldo disponible: {self.income}')
                


def ingresos():
    list_ingresos = []
    for i in range(2000, 5000, 12):
        list_ingresos.append(i)
    income = choice(list_ingresos)
    return income

def make_customer(income):
    system('cls')
    print('                             BANCO                              ')
    name = input('Ingresa tu nombre: ').title()
    last_name = input('Ingresa tu apellido: ').title()
    number_count = int(input('Ingresa tu numero de cuenta: '))
    system('cls')
    cliente_1 = Cliente(name, last_name, number_count, income)
    return cliente_1

def choice_action():
    print('\nQue Transaccion quieres realizar?\n')
    transaction = int(input('''[1] - Depositar
[2] - Retirar
'''))
    return transaction
          
def return_main_menu():
    input("\nPresiona Enter para regresar al menú principal")

while True:
    income = ingresos()
    make_user = make_customer(income)
    print(make_user)
    transaction = choice_action()
    system('cls')
    if transaction == 1:
        make_user.deposit()
        return_main_menu()
    elif transaction == 2:
        make_user.withdraw()
        return_main_menu()
        