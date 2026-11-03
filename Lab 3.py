from script3 import dishes

print("--- Завдання 1 ---")
sequence = list(map(int, input("Введіть елементи послідовності через пробіл: ").split()))
m = int(input("Введіть ціле число m: "))

print(f"\nПари чисел, сума яких дорівнює {m}:")
found = False

for i in range(len(sequence)):
    for j in range(i + 1, len(sequence)):
        if sequence[i] + sequence[j] == m:
            print(f"({sequence[i]}, {sequence[j]})")
            found = True

if not found:
    print(" таких пар не знайдено.")


print("--- Завдання 2 ---")
total_calories_all = 0

for i, dish in enumerate(dishes, start=1):
    drink_cal = dish["calorie_drink"]
    food_cal = dish["calorie_food"]
    total_dish_cal = drink_cal + food_cal
    total_calories_all += total_dish_cal
    
    print(f"Обід {i} ({dish['drink']} + {dish['food']}): "
          f"напій — {drink_cal} ккал, їжа — {food_cal} ккал, "
          f"всього — {total_dish_cal} ккал")

print(f"\nЗагальна сума калорій усіх страв: {total_calories_all} ккал")
