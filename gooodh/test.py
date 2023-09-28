import csv
with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    names = ["Имя", "Возраст"]
    file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
    file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
    file_writer.writerow({"Имя": "Вова", "Возраст": "14"})