# Імпортуємо бібліотеку PuLP
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Створюємо модель
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні рішення: кількість виробленого лимонаду та фруктового соку
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')  # Кількість лимонаду
fruit_juice = LpVariable("FruitJuice", lowBound=0, cat='Integer')  # Кількість фруктового соку

# Цільова функція: максимізувати загальну кількість продуктів
model += lpSum([lemonade, fruit_juice]), "Total_Products"

# Обмеження
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")  # Вода
model += (1 * lemonade <= 50, "Sugar_Constraint")  # Цукор
model += (1 * lemonade <= 30, "LemonJuice_Constraint")  # Лимонний сік
model += (2 * fruit_juice <= 40, "FruitPuree_Constraint")  # Фруктове пюре

# Розв'язуємо модель
model.solve()

# Виводимо результати
print("Status:", LpStatus[model.status])
print("Кількість виробленого Лимонаду:", value(lemonade))
print("Кількість виробленого Фруктового соку:", value(fruit_juice))
print("Максимальна загальна кількість продуктів:", value(model.objective))