from employees import workers

print("--- Прізвища всіх жінок ---")
for emp in workers:
    if emp["gender"].lower() == "жінка":
        print(emp["surname"])

oldman = None
youngwoman = None

for emp in workers:
    if emp["gender"].lower() == "чоловік":
        if oldman is None or emp["age"] > oldman["age"]:
            oldman = emp
            
    elif emp["gender"].lower() == "жінка":
        if youngwoman is None or emp["age"] < youngwoman["age"]:
            youngwoman = emp

print("\n--- Результати пошуку ---")
if oldman:
    print(f"Найстарший чоловік: {oldman['surname']} ({oldman['age']} років)")
else:
    print("Чоловіків у списку не знайдено.")

if youngwoman:
    print(f"Наймолодша жінка: {youngwoman['surname']} ({youngwoman['age']} років)")
else:
    print("Жінок у списку не знайдено.")
