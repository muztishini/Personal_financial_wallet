from dataclasses import dataclass


@dataclass
class Record:
	date: str
	category: str
	summa: float
	description: str

def add_record():
	date = input("Введите дату: ")
	cat = input("Введите категорию: ")
	summa = float(input("Введите сумму: "))
	desc = input("Введите описание: ")
	rec = Record(date, cat, summa, desc)
	print(rec)

def main():
	print("Какую операцию хотите выполнить:")
	print("1. Вывод баланса")
	print("2. Добавление записи")
	print("3. Редактирование записи")
	print("4. Поиск по записям")
	oper = int(input("? "))
	match oper:
		case 1:
			pass
		case 2:
			add_record()
		case 3:
			pass
		case 4:
			pass
		case _:
			print("Нет такой операции")


if __name__ == "__main__":
	main()
