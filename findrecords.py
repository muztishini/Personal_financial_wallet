def search_record(search_key: str, search_value: str) -> list:
	with open('wallet.txt', 'r') as file:
		lines: list = file.readlines()

	found_records: list = []
	record: dict = {}
	for line in lines:
		if line.strip():
			key, value = line.strip().split('=')
			record[key] = value
		else:
			if record.get(search_key) == search_value:
				found_records.append(record)
			record = {}

	if record.get(search_key) == search_value:
		found_records.append(record)
	return found_records


def find_record() -> None:
	while True:
		search_key: str = input("Введите параметр поиска (0 - Выход): ")
		if search_key == "0":
			return
		search_value: str = input("Введите значение поиска: ")
		found_records: list = search_record(search_key, search_value)
		if found_records:
			print("Найденные записи:\n")
			for item in found_records:
				print(
					f"Дата={item['Дата']}\nКатегория={item['Категория']}\nСумма={item['Сумма']}\nОписание={item['Описание']}\n")
				return
		else:
			print('Запись не найдена.')
