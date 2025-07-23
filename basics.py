# 1. Створи змінні з різними типами: str, int, float, list, dict
text = "Hello"
num = 5
dot = 5.5
lst = [1, "r", True, 23]
dct = dict(name='POUR', am= 1)

# 2. Напиши функцію, яка приймає список чисел і повертає їхню суму
def summa():
    user = input("Enter: ")
    nums = list(map(int, user.split()))
    total = sum(nums)
    print("Сумма: ", total)


summa()

# 3. Створи словник з даними про себе (ім’я, вік, улюблена мова)
I_am = {'name': 'Yuri', 'age': 19, 'lang': 'ukrainian'}

# 4. Напиши цикл, який виводить всі числа від 1 до 10
for i in range(1, 11):
    print(i)


# 5. Напиши цикл, який іде по списку і виводить всі парні числа
nums = [1, 2, 3, 4, 5, 6]

for i in list:
    if i % 2 == 0:
        print(i)
    else:
        print(" ")


# 6. Створи клас Human з полями name та age, методом say_hello()
class Human:
    name = None
    age = None

    def say_hello(self):
        print("Hello")


person = Human()
person.say_hello()