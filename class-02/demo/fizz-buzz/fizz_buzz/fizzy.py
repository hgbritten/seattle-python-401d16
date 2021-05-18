def fizz_buzz(num):
    if num % 3 == 0 and num % 5 != 0:
        num = "Fizz"
        return num
    elif num % 5 == 0 and num % 3 != 0:
        num = "Buzz"
        return num
    elif num % 5 == 0 and num % 3 == 0:
        num = "FizzBuzz"
        return num
    return str(num)
