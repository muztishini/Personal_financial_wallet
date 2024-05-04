class Record:
    def __init__(self, date, cat, summa, desc) -> None:
        self.date = date
        self.cat = cat
        self.summa = summa
        self.desc = desc
        
    def __str__(self) -> str:
        return f"Дата={self.date}\nКатегория={self.cat}\nСумма={self.summa}\nОписание={self.desc}\n"


def balance():
    total_income = 0
    total_expense = 0
    with open('wallet.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Сумма='):
            amount = float(line.split('=')[1])
            if 'Доход' in lines[lines.index(line) - 1]:
                total_income += amount
            elif 'Расход' in lines[lines.index(line) - 1]:
                total_expense += amount
    balance = total_income - total_expense
    print(f"Сумма доходов: {total_income}")
    print(f"Сумма расходов: {total_expense}")
    print(f"Баланс: {balance}")


def add_record():
    date = input("Введите дату: ")
    cat = input("Введите категорию: ")
    summa = float(input("Введите сумму: "))
    desc = input("Введите описание: ")
    rec = Record(date, cat, summa, desc)
    # print(rec)
    with open('wallet.txt', "a") as file:
        file.write(str(rec) + "\n")
        print("Запись добавлена")


def main():
    while True:
        print("Какую операцию хотите выполнить:")
        print("1. Вывод баланса")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск по записям")
        print("0. Выход")
        oper = int(input("? "))
        match oper:
            case 1:
                balance()
            case 2:
                add_record()
            case 3:
                pass
            case 4:
                pass
            case 0:
                break
            case _:
                print("Нет такой операции")


if __name__ == "__main__":
    main()
