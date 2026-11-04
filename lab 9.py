import os
from datetime import datetime, timedelta


file1_name = 'first_file.txt'
file2_name = 'second_file.txt'

with open(file1_name, 'w', encoding='utf-8') as f1:
    f1.write("ЛНУВМБ ім. С. З. Ґжицького")

with open(file2_name, 'w', encoding='utf-8') as f2:
    pass  

print(f"Створено файли: '{file1_name}' та '{file2_name}' у каталозі: {os.getcwd()}")

with open(file1_name, 'r', encoding='utf-8') as src:
    content = src.read()

with open(file2_name, 'w', encoding='utf-8') as dst:
    dst.write(content)

print("Дані успішно скопійовано з першого файла у другий.")

with open(file2_name, 'r', encoding='utf-8') as dst:
    copied_data = dst.read()

print(f"\nВміст другого файла після копіювання:\n{copied_data}\n")

if os.path.exists(file1_name):
    os.remove(file1_name)
    print(f"Файл '{file1_name}' було успішно видалено.")



current_datetime = datetime.now()
print("Поточна дата і час:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

happy = datetime(2006, 10, 23)

birth_date_str = happy.strftime("%Y-%m-%d")

days_of_week = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]
birth_weekday = days_of_week[happy.weekday()]

target_days = 13330
target_date = happy + timedelta(days=target_days)
target_date_str = target_date.strftime("%Y-%m-%d")

results = [
    f"Яка дата вашого народження?: {birth_date_str}",
    f"У який день тижня ви народилися?: {birth_weekday}",
    f"Коли вам буде (або вже було) 13 330 днів від народження?: {target_date_str}"
]

file_name = "birth_info.txt"
with open(file_name, 'w', encoding='utf-8') as f:
    for line in results:
        f.write(line + '\n')
        print(line)  

print(f"\nДані успішно записано у файл '{file_name}'.")
