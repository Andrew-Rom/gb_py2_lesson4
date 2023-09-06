"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


def main_menu():
    while True:
        print('ATM main menu.\n'
              'Balance of your card is ', card_balance, '\n'
                                                        'Select operation:\n'
                                                        '1 - Add funds\n'
                                                        '2 - Withdraw funds\n'
                                                        '0 - Exit and return card')
        operation = input('> ')
        match operation:
            case '1':
                cash = get_amount()
                if cash == -1:
                    print('You entered incorrect amount')
                else:
                    hold_tax()
                    add_funds(money=cash)

            case '2':
                cash = get_amount()
                if cash == -1:
                    print('You entered incorrect amount')
                elif cash > card_balance:
                    print('Your card balance is less than the amount entered')
                else:
                    hold_tax()
                    withdraw_funds(money=cash)
            case '0':
                print('Thank you for using our ATM.')
                print(operations)
                exit()
            case _:
                print('Incorrect selection. Please, try again \n')


def get_amount():
    amount = input('Enter the amount > ')
    return int(amount) if amount.isdigit() and int(amount) % 50 == 0 else -1


def add_funds(money: int):
    global operation_counter, card_balance, operations
    temp = card_balance
    card_balance += money
    operations.append(('add funds', temp, money, card_balance))
    operation_counter += 1
    if operation_counter == BONUS_CONDITION:
        operation_bonus()


def withdraw_funds(money: int):
    global operation_counter, card_balance, operations
    temp = card_balance
    atm_fee = money * ATM_INTERESTS
    if atm_fee < ATM_INTERESTS_MIN:
        atm_fee = ATM_INTERESTS_MIN
    if atm_fee > ATM_INTERESTS_MAX:
        atm_fee = ATM_INTERESTS_MAX
    if card_balance >= money + atm_fee:
        card_balance -= (money + atm_fee)
        operations.append(('withdraw funds', temp, money, atm_fee, card_balance))
        operation_counter += 1
        if operation_counter == BONUS_CONDITION:
            operation_bonus()
    else:
        print('You do not have enough funds in your account to make the operation.')


def operation_bonus():
    global card_balance, operation_counter, operations
    temp = card_balance
    card_balance += card_balance * BONUS
    operations.append(('pay bonus', temp, card_balance * BONUS, card_balance))
    operation_counter = 0


def hold_tax():
    global card_balance, operations
    temp = card_balance
    if card_balance > TAX_CONDITION:
        card_balance -= card_balance * TAX_RATE
        operations.append(('pay tax', temp, card_balance * TAX_RATE, card_balance))


BONUS = 3 / 100
BONUS_CONDITION = 3

TAX_RATE = 10 / 100
TAX_CONDITION = 5_000_000

ATM_INTERESTS = 1.5 / 100
ATM_INTERESTS_MIN = 30
ATM_INTERESTS_MAX = 600

card_balance = 0
operation_counter = 0
operations = []

main_menu()
