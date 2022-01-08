# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

print("Задание №1")
a = 8
b = a + 1
print(b)

a = -3
b = 4
c = a + b
print(c)

name = "Ася"
print("Меня зовут", name)
age = 30
print("Меня зовут", name, "Мне", age, "лет")
name2 = input("Введите ваше имя:")
age2 = int(input("Введите ваш возраст: "))

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print ("Задание №2")
seconds = int(input("Секунды: "))
hours = seconds // 3600
left = seconds % 3600
minutes = left // 60
second = left % 60
print(f"Это: {hours}:{minutes}:{second}")


# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print ("Задание №3")
n = input("Введите число")
m = int(n + n)
l = int(n + n + n)
p = int(n) + m + l
print(p)


# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print ("Задание №4")
new_number = input("Введите число: ")
g = 0
for i in new_number:
    while int(i) > g:
        g = int(i)
print(g)



# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print ("Задание №5")
receipts = int(input("Введите вашу выручку: "))
expenses = int(input("Введите ваши издержки: "))

if receipts > expenses:
    profitability = receipts - expenses
    print(f"Выручка больше издержек и составляет {profitability}")
    workers = int(input("Сколько человек работает в компании: "))
    print(f"{profitability / workers} на одного человека")
    if receipts == expenses:
        print("Прибыли нет, выручка равна издержкам")
    elif receipts < expenses:
        loss = expenses - receipts
        print(f"Издержек больше прибыли, компания работает в убыток. Убыток составляет: {loss}")



