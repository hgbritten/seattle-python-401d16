class Dog:
    def __init__(
        self,
        name="unknown",
    ):
        self.name = name

    def sleep(self):
        return "zzz"


class Boxer(Dog):
    def greet(self):
        return f"The name's {self.name}. Pleasure"


class Puggle(Dog):
    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"


def matrix(list):
    new_list = []
    for i in list:
        new_value = 0
        for j in i:
            new_value += i[j]
        new_list.append(new_value)
    return new_list


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 1 + 0 = 1
# 1 +


def fibonacci_iterative(n, x=0, y=1):
    if n <= 1:
        return n
    else:
        total_sum = 0
        while n >= 0:
            sum = x + y
            total_sum += sum
            n - 1
        return total_sum
