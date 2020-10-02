a = int(input('Введи первое число '))
b = int(input('Введи второе число '))

def fun_1():
    try:
        x = a / b
    except ZeroDivisionError:
        print('Деление на ноль, перезапустите программу')
    return x
x = fun_1()
print(x)
