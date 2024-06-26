from findrecords import find_record


# функция редактирования записи
def edit_record() -> None:
	while True:
		print("Какую запись хотите отредактировать? ")
		find_record()

		with open('wallet.txt', 'r') as file:
			lines = file.readlines()

		search_lines: str = input("Введите строку для редактирования (0 - Выход): ")
		if search_lines == "0":
			return
		new_line: str = input("Введите новую строку: ")
		index: int = -1
		for i, line in enumerate(lines):
			if search_lines in line:
				index = i
				break
		if index != -1:
			lines[index] = f'{new_line}\n'

		with open('wallet.txt', 'w') as file:
			file.writelines(lines)
			print("Запись успешно отредактирована")
			return
