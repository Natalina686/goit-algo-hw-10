import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
def monte_carlo_integration(func, a, b, num_samples=10000):
    # Генерація випадкових точок
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)
    
    # Підрахунок кількості точок, що потрапили під графік
    under_curve = np.sum(y_random < func(x_random))
    
    # Обчислення площі
    area = (b - a) * (f(b)) * (under_curve / num_samples)
    return area

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)

# Обчислення інтеграла за допомогою scipy.integrate.quad
quad_result, _ = quad(f, a, b)

# Виведення результатів
print(f"Результат методу Монте-Карло: {monte_carlo_result}")
print(f"Результат функції quad: {quad_result}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
