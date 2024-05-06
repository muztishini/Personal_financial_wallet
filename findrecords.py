def search_record(search_key, search_value):
	with open('wallet.txt', 'r') as file:
		lines = file.readlines()

	found_records = []
	record = {}
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


def find_record():
	while True:
		search_key = input("Введите параметр поиска (0 - Выход): ")
		if search_key == "0":
			break
		search_value = input("Введите значение поиска: ")
		# search_key = "Сумма"
		# search_value = '23.0'
		found_records = search_record(search_key, search_value)
		if found_records:
			print("Найденные записи:\n")
			for item in found_records:
				print(
					f"Дата={item['Дата']}\nКатегория={item['Категория']}\nСумма={item['Сумма']}\nОписание={item['Описание']}\n")
		else:
			print('Запись не найдена.')
